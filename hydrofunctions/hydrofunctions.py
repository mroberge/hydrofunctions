# -*- coding: utf-8 -*-


def first():
    print("This is the first function.")
    return True


if __name__ == '__main__':
    import subprocess
    import sys
    from contextlib import contextmanager
    import os


    def run_cmd():
        print("Press Cntl-C to exit this command")
        cmd = "nose2"
        ## run it ##
        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

        ## But do not wait till netstat finish, start displaying output immediately ##
        while True:
            out = p.stderr.read(1)
            if out == '' and p.poll() != None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()


    @contextmanager
    def cd(newdir):
        prevdir = os.getcwd()
        os.chdir(os.path.expanduser(newdir))
        try:
            yield
        finally:
            os.chdir(prevdir)


    with cd('..'):
        run_cmd()  ## This requires that you end with ctrl-C
