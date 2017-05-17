printf %"s\n" 'Testing CPU Bound Thread Performance'
function liner {
    for i in `seq $1`;do echo -n =-;done
    printf %"s\n" =
}
liner 38
printf %"s\n" 'Testing Serial Program'
python2.7 serial.py
python3.6 serial.py
printf %"s\n" 'Testing Multithreading...'
python2.7 mthreading.py 1
python2.7 mthreading.py 2
python2.7 mtspin.py 2
python2.7 mthreading.py 4
python2.7 mthreading.py 6
python2.7 mthreading.py 8
python2.7 mthreading.py 16
liner 5
python3.6 mthreading.py 1
python3.6 mthreading.py 2
python3.6 mtspin.py 2
python3.6 mthreading.py 4
python3.6 mthreading.py 6
python3.6 mthreading.py 8
python3.6 mthreading.py 16
echo "Please press Enter to continue.."
read input
printf %"s\n" 'Testing MultiProcessing ...'
python2.7 mprocessing.py 1
python2.7 mprocessing.py 2
python2.7 mprocessing.py 4
python2.7 mprocessing.py 6
python2.7 mprocessing.py 8
python2.7 mprocessing.py 16
liner 5
python3.6 mprocessing.py 1
python3.6 mprocessing.py 2
python3.6 mprocessing.py 4
python3.6 mprocessing.py 6
python3.6 mprocessing.py 8
python3.6 mprocessing.py 16
liner 38
