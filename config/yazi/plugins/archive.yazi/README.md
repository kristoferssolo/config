# archive.yazi

A Yazi plugin that compresses selected files to an archive.

## Supported file types

| Extention     | Unix Command  | Windows Command |
| ------------- | ------------- | --------------- |
| .zip          | zip -r        | 7z a -tzip      |
| .7z           | 7z a          | 7z a            |
| .tar          | tar rpf       | tar rpf         |
| .tar.gz       | gzip          | 7z a -tgzip     |
| .tar.bz2      | bzip2         | 7z a -tbzip2    |
| .tar.xz       | xz            | 7z a -txz       |


**NOTE:** Windows users are required to install 7-Zip and add 7z.exe to the `path` environment variable, only tar archives will be available otherwise.


## Install

```bash
# For Unix platforms
git clone https://github.com/KKV9/archive.yazi.git ~/.config/yazi/plugins/archive.yazi

## For Windows
git clone https://github.com/KKV9/archive.yazi.git %AppData%\yazi\config\plugins\archive.yazi

# Or with yazi plugin manager
ya pack -a KKV9/archive
```

- Add this to your `keymap.toml`:

```toml
[[manager.prepend_keymap]]
on   = [ "c", "a" ]
run  = "plugin archive"
desc = "Archive selected files"
```

## Usage

 - Select files or folders to add, then press `c` `a` to create a new archive.
 - Type a name for the new file. 
 - The file extention must match one of the supported filetype extentions.
 - The desired archive/compression command must be installed on your system.
