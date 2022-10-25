######
# TREENODE CLASS
######
print("Once upon a time...")

class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while story_node.choices != []:
      choice = int(input("What do you do? Choose 1 or 2: "))
      if choice in [1, 2]:
        chosen_index = choice - 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child
      else:
        print("Invalid choice.")



user_name = input("What is yout name? ")
print(user_name)

######
# VARIABLES FOR TREE
######

story_root = TreeNode(f"""
{user_name}, you are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
story_root.add_child(choice_a)

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
story_root.add_child(choice_b)

choice_a_a = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a.add_child(choice_a_a)

choice_a_b = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.
 
YOU REMAIN LOST.
""")
choice_a.add_child(choice_a_b)

choice_b_a = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
""")
choice_b.add_child(choice_b_a)

choice_b_b = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_b.add_child(choice_b_b)

######
# TESTING
######

story_root.traverse()
