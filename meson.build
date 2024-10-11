project('datastoragelease',
  'c',
  version: '1.0.0',
  license: 'GPL-3',
  meson_version: '>= 1.5.2',
  default_options: [
    'c_std=c17',
  ],
)

py = import('python').find_installation(pure: false)

install_subdir('src/datastoragelease', install_dir : py.get_install_dir(pure: false))