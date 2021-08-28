#!/usr/bin/python3
""".tgz file obtained from web_static dir"""

from datetime import datetime
from re import T
from fabric.api import local, put, run, env
from os import path


env.hosts = ['34.138.86.55', '34.75.178.179']
env.packed_file = None


def do_pack():
    """ generates a .tgz fiile with the content of the wen_static folder"""
    folder_name = "versions"
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

    # creates if not exist, the folder verdions
    local("mkdir -p {}".format(folder_name))

    # creates the packed file
    path = "{}/web_static_{}.tgz".format(folder_name, time)
    r = local("tar -czf {} web_static".format(path), capture=True)
    if r.failed:
        return None
    return path


def do_deploy(archive_path):
    """ deploy an cipped file in the server """

    full_filename = archive_path.split('/')[-1]
    filename = full_filename.rsplit('.', 1)[0]
    remote_path = "/data/web_static/releases/{}/".format(filename)
    temp_path = '/tmp/'

    if not path.exists(archive_path):
        return False

    try:
        # send the file to the server
        put(archive_path, remote_path=temp_path)

        # subtract the files in the specific folder
        run('mkdir -p ' + remote_path)
        run('tar -xzf ' + temp_path + full_filename + ' -C ' + remote_path)
        run('mv ' + remote_path + 'web_static/* ' + remote_path)
        run('rm -rf ' + remote_path + 'web_static')

        # delete the file from /tmp/
        run("rm " + temp_path + full_filename)

        # removes and re creates the symbolic link
        run("rm /data/web_static/current")
        run("ln -s " + remote_path + " /data/web_static/current")
        return True
    except Exception as err:
        return False


def deploy():
    """ Perform a complete deploy """
    if env.packed_file is None:
        env.packed_file = do_pack()
    print(env.packed_file)
    if env.packed_file is None:
        return False

    return do_deploy(env.packed_file)


def do_clean(number=0):
    """ Remove previous files in local and servers """
    number = int(number)
    if number == 0:
        number = 1
    # list the local files in folder versions
    ls = local("ls -1t versions/", capture=True)
    ls = ls.splitlines()

    # traverse the list
    for index in range(number, len(ls)):
        full_filename = ls[index]
        filename = full_filename.rsplit(".", 1)[0]
        filename = "/data/web_static/releases/" + filename

        # remove each file in local and each folder in remote
        local("rm -f versions/" + full_filename)
        run("rm -rf " + filename)
