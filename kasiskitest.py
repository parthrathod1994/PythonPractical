import itertools, re
NONLETTERS_PATTERN = re.compile('[^A-Z]')

def findRepeatSequencesSpacings(message):

    # remove non-alphabet from the message.
    message = NONLETTERS_PATTERN.sub('', message.upper())

    print("Message=",message)

    seqSpacings = {}
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            # store it in seq those found as a repeatation
            seq = message[seqStart:seqStart + seqLen]
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                # Found a repeated sequence.
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []

                    seqSpacings[seq] = i - seqStart
    return seqSpacings

ciphertext = 'Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf,Adiz kdmktsvmztsl, izr xoexghzr kkusitaafADI.'
repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

#print("repeateData=",repeatedSeqSpacings)

for i in repeatedSeqSpacings:
    print(i,"=",repeatedSeqSpacings[i])