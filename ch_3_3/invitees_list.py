invitees = ["N1", "N2", "N3"]
invitation_1 = f"Dear {invitees[0]}, you are cordially invited to our event."
invitation_2 = f"Dear {invitees[1]}, you are cordially invited to our event."
invitation_3 = f"Dear {invitees[2]}, you are cordially invited to our event."
print(invitation_1)
print(invitation_2)
print(invitation_3)
total_invitees = len(invitees)
print(f"Total number of invitees: {total_invitees}")

invitation_2_updated = f"Dear {invitees[1]}, we regret to inform you that you are unable to attend our event."
print(invitation_2_updated)
total_invitees = len(invitees)
print(f"Total number of invitees: {total_invitees}")

invitees[1] = "M2"
invitation_2 = f"Dear {invitees[1]}, you are cordially invited to our event."
print(invitation_2)
total_invitees = len(invitees)
print(f"Total number of invitees: {total_invitees}")

print("We have found a bigger venue, so we can invite more guests!")
invitees.insert(0,"S1")
invitees.insert(2,"S2")
invitees.append("S3")
print("Updated list of invitees:")
for invitee in invitees:
    print(f"Dear {invitee}, you are cordially invited to our event.")
total_invitees = len(invitees)
print(f"Total number of invitees: {total_invitees}")

print("Unfortunately, due to unforeseen circumstances, we can only invite two guests.")
while len(invitees) > 2:
    removed_invitee = invitees.pop()
    print(f"Dear {removed_invitee}, we regret to inform you that you are unable to attend our event.")
for invitee in invitees:
    print(f"Dear {invitee}, you are still invited to our event.")
total_invitees = len(invitees)
print(f"Total number of invitees: {total_invitees}")

del invitees[1]
del invitees[0]
print("Final list of invitees:", invitees)
total_invitees = len(invitees)
print(f"Total number of invitees: {total_invitees}")