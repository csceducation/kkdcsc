def global_context(request):
    return {
        "company": "Karaikudi",
        "user_ip": request.META.get("REMOTE_ADDR", "Unknown"),
    }
    
company = "Karaikudi"
site_pass = "630003"
uname = "kkdcsc"