# bilibili_backup

backup bilibili collection videos

## Prerequisite

* python3
* tqdm
* you-get

```bash
pip install you-get
```

## Usage

1. Clone the repository

```bash
git clone https://github.com/crh19970307/bilibili_backup.git
cd bilibili_backup
```

2. Open the bilibili collection you want to backup in browser. F12->Console->copy the javascript code `getlist.js` and run. Then you will get a list. Copy the content and paste it to `download.txt`.

3. Specify the output folder `OUTPUT_DIR` in `download.py`, then run the code

```bash
python download.py
```

4. Just wait!

## License

GNU General Public License v3.0

## Claim

Crawling too fast may cause ip blocking. Even single process may fail sometimes, so multiprocessing accelerating is deprecated.

If some videos fail to download, just rerun `download.py`. It will not duplicatedly download the videos that have been successfully downloaded.
