from pyfingerprint.pyfingerprint import PyFingerprint

try:
    # Initialize the sensor (port, baud rate, address, password)
    sensor = PyFingerprint('*ELAN7001', 57600, 0xFFFFFFFF, 0x00000000)

    if not sensor.verifyPassword():
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

print('Currently stored templates: ' + str(sensor.getTemplateCount()) + '/' + str(sensor.getStorageCapacity()))

# Enroll a new fingerprint
def enroll_fingerprint():
    try:
        print('Waiting for finger...')
        while not sensor.readImage():
            pass

        sensor.convertImage(0x01)
        result = sensor.searchTemplate()
        positionNumber = result[0]

        if positionNumber >= 0:
            print('Fingerprint already exists at position #' + str(positionNumber))
            return

        print('Remove finger...')
        while sensor.readImage():
            pass

        print('Waiting for the same finger again...')
        while not sensor.readImage():
            pass

        sensor.convertImage(0x02)

        if sensor.compareCharacteristics() == 0:
            raise Exception('Fingers do not match')

        sensor.createTemplate()
        positionNumber = sensor.storeTemplate()
        print('Fingerprint enrolled successfully at position #' + str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

# Authenticate a fingerprint
def authenticate_fingerprint():
    try:
        print('Waiting for finger...')
        while not sensor.readImage():
            pass

        sensor.convertImage(0x01)
        result = sensor.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No match found!')
        else:
            print('Match found at position #' + str(positionNumber))
            print('Access granted!')

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

# Main execution
if __name__ == '__main__':
    print("1. Enroll a new fingerprint")
    print("2. Authenticate a fingerprint")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        enroll_fingerprint()
    elif choice == '2':
        authenticate_fingerprint()
    else:
        print("Invalid choice")
