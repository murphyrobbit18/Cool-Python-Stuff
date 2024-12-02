# Hardware Reading Functions Pseudocode 
```markdown
y = 3

func getAccel(y)
  samps =  readings from three axis accelerator

  sampY = empty list
  for i in range of y
    add a value from samps to sampY

  aveList = sum of the values / length of the values

  if aveList < 0
    is True

  else
    is False

func rotary_dial
  rotary_pos = reading of rotary dial

  if rotary_pos is equal to zero
    is True
  else
    is False

func getLEDReading()
  reading = button press reading

  if there is a reading
    is True
  else
    is False
