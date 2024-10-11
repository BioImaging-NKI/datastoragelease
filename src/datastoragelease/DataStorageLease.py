import tomllib
from pathlib import Path
import os
import logging
from datetime import date
import win32com.client as com


def datastoragelease() -> None:
    logger = logging.getLogger("DataStorageLease")
    pth = Path(Path.cwd(), 'DataStorageLease.toml')
    if not pth.exists():
        logger.error("No DataStorageLease.toml file was found.")
        return
    with open(pth, 'rb') as fp:
        data = tomllib.load(fp)

    if data['PC'] != os.environ['COMPUTERNAME']:
        logger.error(f"Storage file for {data['PC']} will not run on {os.environ['COMPUTERNAME']}")
        return
    ignore = ['$RECYCLE.BIN', 'System Volume Information']
    folders = [x for x in Path.cwd().glob('*') if x.is_dir()]
    for k in data.keys():
        if k not in folders:
            logger.warning(f"There is no folder for {k}.")
    for folder in folders:
        if folder in ignore:
            continue
        if folder.name not in data.keys():
            logger.warning(f"There is no lease for {folder.name}.")
        else:
            if data[folder.name]['untill'] < date.today():
                logger.warning(f"Data lease for {folder.name} has expired.")
            else:
                foldersize = sizeoffolder(folder)
                bytesallowed = converttobytes(data[folder.name]['amount'])
                if foldersize > bytesallowed:
                    logger.warning(f"{folder.name} has exceeded the allowed storage.")
                else:
                    logger.info(f"{folder.name} ok")



def sizeoffolder(pth: Path) -> int:
    fso = com.Dispatch("Scripting.FileSystemObject")
    folder = fso.GetFolder(str(pth))
    return folder.Size
    # return sum(f.stat().st_size for f in pth.glob('**/*') if f.is_file())


def converttobytes(text: str) -> int:
    strfind = ['kb', 'mb', 'gb', 'tb', 'eb']
    unit = [i for i, x in enumerate(strfind) if x in text.casefold()]
    return int(text[0:-2]) * 10 ** ((1 + unit[0]) * 3)
