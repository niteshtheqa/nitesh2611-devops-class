#! /bin/bash
set -x
#Print First name 
DATARECORD="last=Clifford,first=Johnny Boy,state=CA"
COMMA1=index "$DATARECORD" ',' # 14 position of first comma

echo "$COMMA1"