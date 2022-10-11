# Alter-Ego

A content moderation scheme for social media

## Accounts

An account is a user in the system.
A person may have multiple accounts, and an account may be shared my multiple people.
An account may be controlled by real people or automated (bots). Accounts are the sources of messages.

### Follows

An account may follow any number of other accounts.
Followed accounts may be organized into any number of lists.
Each account has a default follow list named `main`.

Follow lists may be public (readable by all) or private (readable by selected accounts or lists).

### Blocks

An account may block any number of other accounts.
Blocked accounts may be organized into any number of lists.
Each account has a default block list named `main`.

Block lists may be public (readable by all) or private (readable by selected accounts or lists).

### Subscriptions

An account may subscribe to any number of follow lists and block lists published by other accounts.
An account follows all the accounts in the subscribed follow lists except for the ones directly and indirectly blocked.
An account blocks all the account in the subscribed block lists except for the ones directly followed.

Let's say there are five accounts: A, B, C, D, E.
Account A follows B and blocks C.
Additionally A subscribes to a follow list including {C, D, E} and subscribes to a block list including {B, C, D}.
Effectively A follows B and E because C and D are blocked.
Effectively A blocks only C and D because B is directly followed.

## Messages

A message is a discrete piece of content sent by an account.
A message may be public (readable by all accounts) or private (readable by selected accounts or lists).

There are two types of messages, posts and replies. 
Posts are stand-alone messages.
Replies are messages that reference another message.
Posts and replies may have any number of replies.

### Top-level Messages

Top-level messages are posts and replies that have been promoted to the top by an account.
Promoting is similar to retweeting (RT) and quote tweeting (QT) on Twitter.

### Timelines

A timeline for an account includes all the top-level messages from accounts that are followed and not blocked.
An account may view replies of messages if they are not blocked.
A message is blocked if the author is blocked or if it refers to a message that is blocked, recursively.

Extending the example above, let's say accounts B, C, D, and E all post top-level messages.
Account A's timeline will only include the posts from B and E even though A subscribes to a follow list that includes all because the block lists override the follows.
