# compile the final code samples for the chapterapters

echo "compiling files in chapter 1"
cd chapter1; compile.sh
cd -
echo "compiling files in chapter 2"
cd chapter2; compile.sh
cd -
echo "compiling files in chapter 3"
cd chapter3; compile.sh
cd -
echo "compiling files in chapter 4"
cd chapter4; compile.sh
cd -
echo "compiling files in chapter 5"
cd chapter5; compile.sh
cd -
echo "compiling files in chapter 6"
cd chapter6; compile.sh
cd -
echo "compiling files in chapter 7"
cd chapter7; compile.sh
cd -
echo "compiling files in appendix"
cd appendix; compile.sh
cd -

