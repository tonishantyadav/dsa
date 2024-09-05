# Intuition:
"""
  s = "Let's take LeetCode contest"
  s.split() -> ['Let\'s', 'take', 'LeetCode', 'contest']
  [::-1] -> ['contest', 'LeetCode', 'take', 'Let\'s']
  ' '.join -> 'contest LeetCode take Let\'s'
  [::-1] -> "s'teL ekat edoCteeL tsetnoc"

"""


def reverseWords(s: str) -> str:
    return " ".join(s.split()[::-1])[::-1]


s = "Let's take LeetCode contest"
result = reverseWords(s)
print(result)
