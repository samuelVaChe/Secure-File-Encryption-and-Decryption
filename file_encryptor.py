import subprocess

def encrypt_file(input_file, output_file, passphrase):
    subprocess.run(['openssl', 'enc', '-aes-256-cbc', '-salt', '-in', input_file, '-out', output_file, '-k', passphrase])

def decrypt_file(input_file, output_file, passphrase):
    subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-in', input_file, '-out', output_file, '-k', passphrase])

if __name__ == '__main__':
    input_file = 'sample.txt'
    encrypted_file = 'encrypted_sample.txt'
    decrypted_file = 'decrypted_sample.txt'
    passphrase = input('Enter passphrase: ')

    encrypt_file(input_file, encrypted_file, passphrase)
    print('File encrypted.')

    decrypt_file(encrypted_file, decrypted_file, passphrase)
    print('File decrypted.')
