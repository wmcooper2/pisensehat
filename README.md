# Logging stats
The pi will sit on a table undisturbed to get a baseline.
All sampling includes a timestamp.

## Maximum sampling ability; all sensors, no delay
Sampling size: 500
Function 1; includes name fields, data rounded to 3 places.
Function 2; no name fields, data rounded to 3 places.
Function 3; no name fields, data not rounded.

Stats recorded:
  * Time (seconds)
  * Size (bytes)

`loggingdata.py`: saving data as strings.

    Function 1      Function 2      Function 3
    ==========      ==========      ========== 
    38.056487       37.69859        37.595765
    187489          84860           180732

`loggingdata_bytes.py`: saving data as bytes.

    Function 1      Function 2      Function 3
    ==========      ==========      ==========
    38.049455       37.684486       37.805761
    187483          84796           180735

`loggingdata_csv.py`: saving data as comma separated values.

    Function 1      Function 2      Function 3
    ==========      ==========      ==========
    38.022449       37.601521       37.584205
    195728          65347           161634
Result: rounding the data decreases the size of the file, but there is no significant change in sampling time.

## Just movement sensors, no delay
Orientation, compass, acceleration, gyroscope
_Sampling size: 500_
No rounding of floats.
Time: 34.162627
Size: 134434 

Rounded to 3 places.
Time: 34.207844
Size: 53356

_Sampling size: 10,000_
No rounding of floats.
Time: 684.73154 
Size: 2668209

Rounded to 3 places.
Time: 685.062453
Size: 1069480

## Single sensor sampling abiilty, no delay
Sampling size: 10,000

### temperature
Time: 8.191278
Size: 709593

### humidity
Time: 8.586165
Size: 720792

### pressure
Time: 8.502444
Size: 704664

### magnetometer, xyz
Time: 8.586165
Size: 720792

### accelerometer, xyz
Time:
Size:

### orientation, xyz
Time:
Size:

### gyroscope, xyz
Time:
Size:
