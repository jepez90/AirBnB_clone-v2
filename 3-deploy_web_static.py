#!/usr/bin/python3
""".tgz file obtained from web_static dir"""

from datetime import datetime
from re import T
from fabric.api import local, put, run, hosts, env


# env.hosts=['ubuntu@34.138.86.55', 'ubuntu@34.75.178.179']

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
    return r


@hosts('ubuntu@34.138.86.55', 'ubuntu@34.75.178.179')
def do_deploy(archive_path):
    """ deploy an cipped file in the server """
    remote_path = "/data/web_static/releases/"
    temp_path = '/tmp/'
    full_filename = archive_path.split('/')[-1]
    filename = full_filename.rsplit('.', 1)[0]
    try:
        # send the file to the server
        result = put(archive_path, remote_path=temp_path)
        if len(result) == 0:
            return False
        # subtract the files in the specific folder
        run('mkdir -p ' + remote_path + filename + '/')
        run('tar -xzf ' + temp_path + full_filename +
            ' -C ' + remote_path + filename + '/')
        run('mv ' + remote_path + filename +
            '/web_static/* ' + remote_path + filename + '/')
        run('rm -rf ' + remote_path + filename + '/web_static')

        # delete the file from /tmp/
        run("rm " + temp_path + full_filename)

        # removes and re creates the symbolic link
        run("rm /data/web_static/current")
        run("ln -sf " + remote_path + filename + " /data/web_static/current")
        return True
    except Exception as err:
        return False


def deploy():
    packed_file = do_pack()
    print(packed_file)
    if packed_file is None:
        return False

    return do_deploy(packed_file)
