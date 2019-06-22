# Flat

Quick Cloud-Storage communication program

## Why I made it

I was looking for a quick way to communicate between my virtual linux server and laptop. There are dozens of alternatives that let me move files around, but I needed something that has more extensibility. Hence I made a quick sketch and crafted up some codes here in haste.

## Download

```
$ git clone https://github.com/chiantiscarlett/flat.git
```

## Quick Usage

```bash
$ python3 main.py DIRECTION --from [PATH] --to [PATH]
```

## Detailed Instruction

Flat supports two types of DIRECTION: download and upload. In the case of **download**, **--from** argument requires remote cloud-storage path, and **--to** argument indicates local path. For the **upload** direction, it is the opposite. **--from** means local path, and **--to** is for the remote cloud-storage path.

```bash
python3 main.py download -f /my/remote/path.mp4 -t /my/local/path.mp4
python3 main.py upload -f /my/local/path.mp4 -t /my/remote/path.mp4
```

Also, you can use 'dl', 'd' instead of 'download', and 'ul', 'u' for the 'upload'. And please do not forget that cloud-storage paths should always start with '/'.

## Initial Settings

### Dropbox

1. Install official Dropbox module

```bash
$ sudo pip3 install dropbox
```

2. Please get your API key from [here](https://www.dropbox.com/developers/apps). Make sure you give **[Full Dropbox] permission** as the type of access permission. Once the app has been created, generate access token which will be used as the KEYS in your settings.json file. There is **no need of applying for production of your app.**

Now open your settings.json file, and set it to the following. Pay attention to the type of the KEYS. It should be in the list type, not a single string.

```json
{
  "SERVER_TYPE": "Dropbox",
  "KEYS": ["YOUR_DROPBOX_API_KEY"]
}
```

## What will be updated in near future

Soon, flat will be enrolled in PyPI and will be pip-installable. Though I don't have time to update frequently, I'll do my best to push full effort in it. Right now, flat only supports Dropbox. But other cloud-storage system including Google Drive will be added in the future.

And in the feature aspects, flat should have folder uploads and folder downloads, as well as alias function that'll spare your time for all these scribbles.
