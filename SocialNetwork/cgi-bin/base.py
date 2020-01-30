#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# print("Content-type: text/html\r\n\r\n")

def header():
    print('''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>SocialHub</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <link rel="stylesheet" href="../design.css">
</head>
<body>''')

def navbar(firstname,email):
  print(f'''  <nav class="navbar navbar-expand-lg" style="background-color: #009baf; color: white;">
        <a class="navbar-brand" href="../index.html">
            <img src="https://socialhub.io/wp-content/uploads/2016/06/SocialHub-Logo-Color-RGB.png" width="200" height="30" class="d-inline-block align-top" alt="">
          </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#"><i class="fas fa-user"></i> {firstname}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Create</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#"><i class="fas fa-users"></i></a>
              </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              </a>
              <div class="dropdown-menu custom-dropdown" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="editProfile.py?firstname={firstname}&email={email}">Edit Profile</a>
                <a class="dropdown-item" href="#">Settings</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Log Out</a>
              </div>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Find Friends" aria-label="Search">
            <button class="btn btn-outline-warning my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </nav>
    ''')

def error(email, errorMsg):
  print(f'''
    <nav class="navbar navbar-light" style="background-color: #009baf;padding-bottom: 0;">
    <div class="row w-100">
        <div class="col-md-3">
            <a class="navbar-brand" href="#" style="margin-top: 20px;">
                <img src="https://socialhub.io/wp-content/uploads/2016/06/SocialHub-Logo-Color-RGB.png" width="200" height="30" class="d-inline-block align-top" alt="">
              </a>
        </div>
        <div class="col-md-5 offset-md-4">
            <form style="color: white;" action="login.py" method="POST">
                <div class="row w-100">
                    <div class="col-md-4">
                        <div class="form-group">
                            <label for="emailBox">Email</label>
                            <input type="email" name="email" id="emailBox" class="form-control" value="{email}">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="form-group" style="margin-bottom: 0;">
                            <label for="passwordBox">Password</label>
                            <input type="password" name="password" id="passwordBox" class="form-control">
                            <a style="font-size: small;">Forgot password ?</a >
                        </div>
                    </div>
                    <div class="col-md-4">
                        <button type="submit" class="btn btn-outline-warning" style="margin-top: 30px;">Log In</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
  </nav>
  <h1 class="text-center" id="error-msg">{errorMsg}</h1>
  <hr>
  ''')

def editProfileForm(firstname,email, profileObject):
  print(f'''
          <div class="container">
          <div class="form-group">
            <button class="btn btn-primary mt-5" data-toggle="modal" data-target="#exampleModal">Change Profile Pic</button>
          </div>
        <form action="updateProfile.py" method="POST" enctype="multipart/form-data">
          <input type="hidden" name="firstname" value="{firstname}">
          <input type="hidden" name="email" value="{email}">
          <div class="form-group">
            <label for="overview">Bio</label>
            <textarea class="form-control mb-2" name="bio" id="overview" rows="5">{profileObject.bio}</textarea>
            <input type="text" class="form-control" placeholder="Nickname" name="nickname" value={profileObject.nickname}>
          </div>
          <div class="form-group">
            <label for="work_education">Work & Education</label>
            <input class="form-control mb-2" type="text" id="work_education" placeholder="Workplace" name="workplace" value="{profileObject.workplace}">
            <input class="form-control mb-2" type="text" placeholder="Professional Skills" name="skills" value="{profileObject.skills}">
            <input class="form-control mb-2" type="text" placeholder="University" name="university" value="{profileObject.university}">
            <input class="form-control" type="text" placeholder="High School" name="school" value="{profileObject.school}">
          </div>
          <div class="form-group">
            <label for="places">Places you've lived</label>
            <input type="text" class="form-control mb-2" id="places" placeholder="Current City" name="current_city"  value="{profileObject.current_city}">
            <input type="text" class="form-control mb-2" placeholder="Home Town" name="hometown"  value="{profileObject.hometown}">
            <input type="text" class="form-control" placeholder="Other Places Lived" name="other_places"  value="{profileObject.other_places}">
          </div>
          <div class="form-group">
            <label for="contact">Contact and basic info</label>
            <input type="text" class="form-control mb-2" name="contact" placeholder="Contact Information" id="contact" value="{profileObject.contact}">
            <select id="dropdown" name="relationship_status" class="form-control" selected="{profileObject.relationship_status}">
              <option value="">Relationship Status</option>
              <option value="single">Single</option>
              <option value="in relationship">In A Relationship</option>
              <option value="engaged">Engaged</option>
              <option value="married">Married</option>
              <option value="complicated">It's Complicated</option>
              <option value="divorced">Divorced</option>
              <option value="widowed">Widowed</option>
            </select>
          </div>
          <div class="form-group">
            <button style="float: right;" type="submit" class="btn btn-primary mb-5">Save Changes</button>
          </div>
        </form>
      </div>
  ''')

def runScript(relationship_status):
  print('''
    <script>
        options = document.getElementById("dropdown").options;
        for(let option of options){''')
  print("if(option.value == '" + relationship_status + "' ) { ")
  print('''option.selected = true
          }
        }
      </script>''')

def profilePicModal(firstname,email):
  print(f'''
  <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog"   aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Change Profile Pic</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" style="padding-bottom: 0">
        <form action="updateProfile.py" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="firstname" value="{firstname}">
          <input type="hidden" name="email" value="{email}">
        <div class="form-group">
            <input type="file" name="profile_pic" id="profile_pic">
          </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="submit" class="btn btn-primary">Save changes</button>
      </div>
      </form>
      </div>
    </div>
  </div>
  </div>
  ''')

def footer():
  print('''
    </body>
    </html>
  ''')