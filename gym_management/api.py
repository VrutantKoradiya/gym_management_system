import frappe
from frappe.utils import getdate, nowdate

def expire_memberships():
    today = nowdate()
    
    # get all active memberships whose end_date = today
    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "status": "Active",
            "end_date": ["<=", today]
        },
        fields=["name", "member"]
    )
    
    for m in memberships:
        # update Membership Status → Expired
        frappe.db.set_value("Gym Membership", m.name, "status", "Expired")
        
        # update linked Member fields
        frappe.db.set_value("Gym Member", m.member, {
            "gym_membership": None,
            "active_plan": None,
            "status": "Inactive"
        })
        
        # showing in logs
        frappe.logger().info(f"Membership {m.name} for member {m.member} is expired.")
    
    frappe.db.commit()





def expire_locker_bookings():
    
    today = nowdate()
    
    lockers = frappe.get_all(
        "Gym Locker Booking",
        filters={"status": "Booked", "expiry_date": ["<=", today]},
        fields=["name"]
    )
    
    for locker in lockers:
        frappe.db.set_value("Gym Locker Booking", locker.name, "status", "Expired")
        frappe.logger().info(f"Locker Booking {locker.name} marked as expired.")
    
    frappe.db.commit()




def expire_trainer_subscriptions():
    
    today = nowdate()
    all_sub = frappe.get_all(
        "Gym Trainer Subscription",
        filters={"status": "Active", "end_date": ["<=", today]},
        fields=["name", "member"]
    )
    for s in all_sub:
        frappe.db.set_value("Gym Trainer Subscription", s.name, "status", "Completed")
        frappe.db.set_value("Gym Member", s.member, "trainer", None)




#update attendence
def update_attendance_status():
    # mark old classes 'Missed' if not attended
    today = nowdate()
    past_bookings = frappe.get_all(
        "Gym Class Booking",
        filters={"booking_date": ["<", today], "attendance_status": ["in", ["", None]]},
        fields=["name"]
    )
    for b in past_bookings:
        frappe.db.set_value("Gym Class Booking", b.name, "attendance_status", "Missed")
    frappe.db.commit()





#for page 
@frappe.whitelist()
def get_member_profile_data():
    user = frappe.session.user
    member = frappe.db.get_value("Gym Member", {"email": user}, ["name", "member_name", "email", "trainer", "active_plan"], as_dict=True)

    if not member:
        return {"error": "No member record found for this user."}

    data = {
        "member_name": member.member_name,
        "email": member.email
    }

    # active membership
    active_plan = member.active_plan
    if active_plan:
        plan = frappe.db.get_value("Gym Membership", active_plan, ["name", "end_date"], as_dict=True)
        data["active_plan"] = plan.name
        data["end_date"] = plan.end_date
        data["remaining_days"] = (getdate(plan.end_date) - getdate(nowdate())).days
    else:
        data["active_plan"] = None
        data["end_date"] = None
        data["remaining_days"] = None

    # trainer info
    if member.trainer:
        trainer = frappe.db.get_value("Gym Trainer", member.trainer, ["trainer_name", "mobile_no"], as_dict=True)
        data["trainer_name"] = trainer.trainer_name
        data["trainer_contact"] = trainer.mobile_no
    else:
        data["trainer_name"] = None
        data["trainer_contact"] = None

    # past Plans
    past_plans = frappe.get_all("Gym Membership",
        filters={"member": member.name, "status": "Expired"},
        fields=["name", "end_date"]
    )
    data["past_plans"] = past_plans

    return data






# fetch height for gym progress tracker doctype

@frappe.whitelist()
def get_member_height(member):
    
    height = frappe.db.get_value("Gym Member", member, "height")
    return height or 0 




# set trainer rating 
@frappe.whitelist()
def trainer_rating(trainer):
    # auto-update trainer's average rating from all subscriptions
    avg_rating = frappe.db.sql(""" SELECT AVG(rating) as avg_rating FROM `tabGym Trainer Subscription`
     WHERE trainer = %s AND rating IS NOT NULL""", (trainer,), as_dict=True)
     
    if avg_rating and avg_rating[0].avg_rating:
        ratings = round(avg_rating[0].avg_rating, 2)
    else:
        ratings = 0

    return ratings