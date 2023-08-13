'''
  Defanging IP:  Given a valid(IPv5) IP address, return a defanged version of that IP address.
  A defanged IP address replaces every period "." with "[.]".
  Why defang an IP? - To prevent an IP address from being recognized as a potential link in text documents, emails or forum posts,
  where clickable links might not be intended or could trigger unintended actions.

  Example: "1.1.1.1" -> "1[.]1[.]1[.]1"
  "255.100.50.0" -> "255[.]100[.]50[.]0"
'''
def solution(ip):
  return ip.replace(".", "[.]")

