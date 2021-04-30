import os
from multiprocessing import Pool, Manager, current_process
import multiprocessing as mp
import subprocess
from tqdm import tqdm
import shutil
import sys

OUTPUT_DIR = "outputs"


def download(name, url):
    if "已失效" in name or "Loading" in name:
        return
    # content = os.popen(f"you-get --no-caption --socks-proxy 127.0.0.1:1234 {url}").read()
    a = subprocess.run(['you-get', '--no-caption', '-O',
                        f"{OUTPUT_DIR}/"+name+'-'+url.split('/')[-1], url], stdout=subprocess.PIPE)
    if a.returncode != 0:
        print(name, url)


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    with open(f"download.txt", "r") as f:
        data = f.readlines()
        names = [i.replace('\n', '').replace('/', '') for i in data[0::2]]
        urls = [i.replace('\n', '') for i in data[1::2]]
        videolist = list(zip(names, urls))
        videolist = [i for i in videolist if ("已失效" not in i[0] and "Loading" not in i[0] and not os.path.exists(
            f"{OUTPUT_DIR}/"+i[0]+'-'+i[1].split('/')[-1]+".mp4"))]
        videolist = videolist[::-1]
        print(f"{len(videolist)} videos to download")
        bar = tqdm(total=len(videolist), position=0)

        def update(*args):
            bar.update()

        for name, url in videolist:
            download(name, url)
            update()
