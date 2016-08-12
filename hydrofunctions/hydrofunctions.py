# -*- coding: utf-8 -*-


def first():
    print("This is the first function.")
    return True

if __name__ == '__main__':
    """
    #sys.exit(unittest.main())
    # sys.exit(nosetests)
    import os
    import subprocess
    return_code = subprocess.call("echo Hello World", shell=True)
    print(return_code)

    print(subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read())
    # print os.popen("echo Hello World").read()
    print(subprocess.Popen("nosetests", shell=True, stdout=subprocess.PIPE).stdout.read())
    stream = os.popen("nosetests")
    print(str(stream))

    return_code = subprocess.call("nosetests", shell=True)
    print(return_code) # returns 1 for failure.
    # run_cmd()  ## This requires that you end with ctrl-C
    # import pytest
    # pytest.main()
    """
    # import nose
    # nose.run()

    import nose2
    #nose2.main(verbosity=2)
    # nose2.main(defaultTest="..")
    nose2.main()
    #nose2.discover.
