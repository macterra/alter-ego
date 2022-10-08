import random

class User:
    def __init__(self, id):
        self.id = id
        self.follows = []
        self.blocks = []
        self.subs = []

    def __repr__(self) -> str:
        return "user {} follows {} blocks {} subs {}".format(self.id, len(self.follows), len(self.blocks), len(self.subs))

    def follow(self, user):
        if user not in self.follows and user.id != self.id:
            self.follows.append(user)

    def block(self, user):
        if user not in self.blocks and user.id != self.id:
            self.blocks.append(user)

    def sub(self, user):
        if user not in self.blocks and user.id != self.id:
            self.subs.append(user)

    def allFollows(self):
        all = set([u.id for u in user.follows])
        for sub in self.subs:
            all |= set([u.id for u in sub.follows])
        all -= set([u.id for u in user.blocks])
        return all

    def allBlocks(self):
        all = set([u.id for u in user.blocks])
        for sub in self.subs:
            all |= set([u.id for u in sub.blocks])
        all -= set([u.id for u in user.follows])
        return all

    def timeline(self, posts):
        myFollows = self.allFollows()
        myBlocks = self.allBlocks()

        print(myFollows)
        for post in posts[::-1]:
            if not post.reply:
                if post.author.id in myFollows:
                    if post.ref and post.ref.isBlocked(myBlocks):
                        print(user.id, post, "blocked")
                    else:
                        print(user.id, post, "visible")
                #else:
                    #print(user.id, post, "not followed")

class Post:
    def __init__(self, users, posts):
        self.author = random.choice(users)
        self.reply = False
        self.ref = 0
        self.replies = []
        self.promotions = []
        if random.random() > 0.1 and len(posts) > 0:
            self.ref = random.choice(posts)
            if random.random() < 0.9:
                self.reply = True
                self.ref.replies.append(self)
            else:
                self.ref.promotions.append(self)
        posts.append(self)
        self.id = len(posts)

    def __repr__(self) -> str:
        if self.ref:
            return "post {} by {} ref {}".format(self.id, self.author.id, self.ref.id)
        else:
            return "post {} by {}".format(self.id, self.author.id)

    def isBlocked(self, blocks):
        print("isBlocked", self, blocks)
        if self.author.id in blocks:
            return True
        if self.ref:
            return self.ref.isBlocked(blocks)
        return False

users = []
for i in range(100):
    users.append(User(i))

for user in users:
    n = random.randint(0, 10)
    for i in range(n):
        user.follow(random.choice(users))
    n = random.randint(0, 10)
    for i in range(n):
        user.block(random.choice(users))
    n = random.randint(0, 10)
    for i in range(n):
        user.sub(random.choice(users))

for user in users:
    print(user)
    print([u.id for u in user.follows])
    print([u.id for u in user.blocks])
    print([u.id for u in user.subs])
    print(user.allFollows())
    print(user.allBlocks())
    print()

posts = []

for i in range(100):
    post = Post(users, posts)
    print(post)

for post in posts:
    print(post, post.replies, post.promotions)

for user in users:
    user.timeline(posts)
