# TRANSPOSITION CIPHER

def do_transposition_cipher(message, key):

    # encrypt this message, okay? <--- BAD JOB FRIENDO

    number_buckets = key
    buckets = [''] * number_buckets

    for column in range(number_buckets):
        index = column

        while index < len(message):
            # drop character in bucket!
            buckets[column] += message[index]

            index += key

    # print(buckets)

    return ''.join(buckets)


if __name__ == "__main__":

    message = """I hopped off the plane at LAX
With a dream and my cardigan
Welcome to the land of fame excess,
Whoa, am I gonna fit in?
Jumped in the cab,
Here I am for the first time
Look to my right and I see the Hollywood sign
This is all so crazy
Everybody seems so famous
My tummy's turnin' and I'm feelin' kinda home sick
Too much pressure and I'm nervous,
That's when the taxi man turned on the radio
And the Jay-Z song was on
And the Jay-Z song was on
And the Jay-Z song was on
So I put my hands up
They're playing my song,
And the butterflies fly away
Noddin' my head like, yeah
Movin' my hips like, yeah
I got my hands up,
They're playin' my song
You know I'm gonna be okay
Yeah, it's a party in the USA
Yeah it's a party in the USA
"""

    message = message.replace('\n', '')
    # encrypt a message
    encrypted_message = do_transposition_cipher(
        message,
        key=16,
    )
    print(encrypted_message)
    print(len(encrypted_message))
    # test: d o iebbegmoyulk ublu?
