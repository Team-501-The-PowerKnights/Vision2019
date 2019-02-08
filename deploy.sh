#!/bin/bash
### deploys vision code to the raspberry pi (tinkerboard)
### must be run from the root of the vision repository

if [ -f util/.ssh/vision_rsa.pub ]; then
   echo "Deploying Vision Code to Raspberry Pi..."
   list=$(find $PWD -type f | grep -vE ".idea|.git|__pycache__")
   pwd=$(pwd)
   cd ..

   for file in $list;
      do
         echo -n "."
         scp -q -i $pwd/util/.ssh/vision_rsa $file linaro@tinkerboard.local:/home/linaro;
         if [ $? -eq 0 ]; then
            code="good"
         elif [ $? -eq 4 ]; then
            code="connect"
            break
         else
            code="fail"
            break
         fi
   done
   if [ "$code" = "connect" ]; then
      echo "Cannot connect. Deploy failed."
   elif [ "$code" = "fail" ]; then
      echo "Deploy failed."
   elif [ "$code" = "good" ]; then
      echo "Success!!!"
   fi
else
   echo "Unable to find ssh keys to deploy. Are you in the root of the vision repository?"
fi
