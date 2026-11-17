from admin import Admin

admin_1 = Admin("Alice", "Johnson", "alice.johnson@example.com")
admin_1.describe_user()
admin_1.privileges.add_privilege("can add post")
admin_1.privileges.add_privilege("can delete post")
admin_1.privileges.add_privilege("can ban user")
admin_1.privileges.show_privileges()