# sgtkcmd

Command line tools for working with ShotGrid Toolkit.

## Installation

```
python setup.py install
```

## Upload Bundles

- Toolkit bundles like apps and frameworks can be uploading using sgtkcmd.
- A config tracked in the bundle repo specifies where to upload the bundle.
- The upload accepts either a zip, or a directory which will be zipped before uploading.
- When uploading a directory, a `.sgignore` file can be used to exclude files and folders.

### Examples

`sgtkcmd-config.yml`

```yaml
upload-bundle:
  # the entity type which contains the bundle file versions
  entity_type: MyCustomEntityType
  # the id of the bundle entity where the new version file should be added
  entity_id: 12345
```

Ignore git directories and sgtkcmd config files, and any other content that should be excluded.

`.sgignore`

```
.git/
sgtkcmd-config.yml
```

From the same directory containing the config, simply run the `upload-bundle` command.

```shell
sgtkcmd upload-bundle
```
