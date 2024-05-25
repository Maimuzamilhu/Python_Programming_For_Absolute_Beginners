"""Advanced Question: Social Media Platform
You are developing a social media platform. Consider the following features:
Users can create posts, comment on posts, and like posts.
Implement a decorator called TagUser that allows users to tag other users in their posts.
Use polymorphism to handle different types of posts (e.g., text, image, video).
Ensure proper encapsulation by protecting user privacy (e.g., private vs. public posts).
Implement error handling for cases like invalid user IDs or missing content.
How would you handle inheritance for user roles (e.g., regular user, admin)?"""

from abc import ABC, abstractmethod

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

class Post(ABC):
    def __init__(self, post_id, content, is_private=False):
        self.post_id = post_id
        self.content = content
        self.is_private = is_private

    @abstractmethod
    def display(self):
        pass

class TextPost(Post):
    def display(self):
        print(f"Text Post ({'Private' if self.is_private else 'Public'}): {self.content}")

class ImagePost(Post):
    def display(self):
        print(f"Image Post ({'Private' if self.is_private else 'Public'}): {self.content}")

class VideoPost(Post):
    def display(self):
        print(f"Video Post ({'Private' if self.is_private else 'Public'}): {self.content}")

def TagUser(post_content):
    # Parse post_content and handle user tagging logic
    # Example: @username -> link to user profile
    pass

# Example usage:
if __name__ == "__main__":
    user1 = User(1, "alice")
    user2 = User(2, "bob")

    text_post = TextPost(101, "Hello, world!", is_private=True)
    text_post.display()

    image_post = ImagePost(102, "image.jpg")
    image_post.display()

    # Apply TagUser decorator to post_content def TagUser(post_content):
    # Assume post_content is a string
    # Parse the content and identify tagged usernames
    # Replace "@username" with links or notifications
    # Return the updated content
    #tagged_content = post_content.replace("@alice", "<a href='/user/alice'>@alice</a>")
    #tagged_content = tagged_content.replace("@bob", "<a href='/user/bob'>@bob</a>")
    #return tagged_content

# Example usage:
post_content = "Check out this photo by @bob! @alice, what do you think?"
updated_content = TagUser(post_content)
print(updated_content)

