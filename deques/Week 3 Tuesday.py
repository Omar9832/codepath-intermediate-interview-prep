from collections import deque




def reverse_memes(memes):
    memes_deque=deque(memes)
    memes_deque.reverse()
    return list(memes_deque)

memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(reverse_memes(memes))
print(reverse_memes(memes_2))
print(reverse_memes(memes_3))




def simulate_meme_reposts(memes, reposts):
    i=0
    while i<len(reposts):
        val=reposts[i]
        while val>1:
            memes.append(memes[i])
            val=val-1
        i=i+1
    return memes

memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"]
reposts = [2, 1, 3]

memes_2 = ["Surprised Pikachu", "This is fine", "Expanding brain"]
reposts = [1, 2, 2]

memes_3 = ["Y U No?", "Philosoraptor"]
reposts = [3, 1]

print(simulate_meme_reposts(memes, reposts))
print(simulate_meme_reposts(memes_2, reposts))
print(simulate_meme_reposts(memes_3, reposts))