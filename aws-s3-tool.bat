@ECHO off
mode con:cols=100 lines=25

::----------
:Start
set LOCAL=Local absolute path
set BUCKET=S3 Bucket name
set AWS_URI=http://acs.amazonaws.com/groups/global/AllUsers
set AWS_ID=AWS Canonical User ID

::----------
CLS
ECHO -----------------------------------------------------------------------------------------------
ECHO LOCAL     %LOCAL%
ECHO BUCKET    %bucket%
ECHO -----------------------------------------------------------------------------------------------
ECHO READY...
PAUSE
goto S3_Sync

::----------
:S3_Sync
ECHO ----------
aws s3 sync %LOCAL% %BUCKET% --delete --grants read=uri=%AWS_URI% full=id=%AWS_ID%
ECHO ----------
ECHO DONE!
PAUSE

::----------
:End
exit