# This file is identical to $PYTHONHOME/Scripts/mitmdump, which apparently you
# can just run by itself on some platforms and it will find it and execute
# this code.  On Windows, however, this folder is not in %PATH% by default.
# Since it's so small it's easier to just reproduce its logic here so we can
# |call| this script instead of `mitmdump`
from libmproxy.main import mitmdump
mitmdump()
