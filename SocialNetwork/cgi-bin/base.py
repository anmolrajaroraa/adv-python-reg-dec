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


def navbar(firstname, email):
    print(f'''  <nav class="navbar navbar-expand-lg" style="background-color: #009baf; color: white;">
        <a class="navbar-brand" href="login.py?firstname={firstname}&email={email}">
            <img src="https://socialhub.io/wp-content/uploads/2016/06/SocialHub-Logo-Color-RGB.png" width="200" height="30" class="d-inline-block align-top" alt="">
          </a>
        <button class="navbar-toggler btn-outline-warning" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="fas fa-bars"></i>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="showProfile.py?firstname={firstname}&email={email}"><i class="fas fa-user"></i> {firstname}</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="createPost.py?firstname={firstname}&email={email}">Create</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="friendsList.py?firstname={firstname}&email={email}"><i class="fas fa-users"></i></a>
              </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              </a>
              <div class="dropdown-menu custom-dropdown" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="editProfile.py?firstname={firstname}&email={email}">Edit Profile</a>
                <a class="dropdown-item" href="#">Settings</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="../index.html">Log Out</a>
              </div>
            </li>
          </ul>
          <div>
            <a href="friendsList.py?firstname={firstname}&email={email}&friend=all">
              <button type="submit" class="btn btn-outline-warning">Find Friends</button>
            </a>
          </div>
        </div>
      </nav>
    ''')


def error(email, errorMsg):
    print(f'''
    <nav class="navbar navbar-light" style="background-color: #009baf;padding-bottom: 0;">
    <div class="row w-100">
        <div class="col-md-3">
            <a class="navbar-brand" href="../index.html" style="margin-top: 20px;">
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


def editProfileForm(firstname, email, profileObject):
    print(f'''
          <div class="container">
          <div class="form-group mt-5">
            <button class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">Change Profile Pic</button>
            <span>{profileObject.profile_pic}</span>
          </div>
        <form action="updateProfile.py?update=true" method="POST" enctype="multipart/form-data">
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


def profilePicModal(firstname, email):
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
            <input type="file" name="profile_pic" id="profile_pic" required> 
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


def showProfile(userObject, profileObject):
    print(f'''
    <div class="container">
        <div class="card mb-3 mt-3" style="max-width: 100%;">
          <div class="row no-gutters">
            <div class="col-md-4 offset-md-1 mt-3">
              <img src="../images/{profileObject.profile_pic}" class="card-img" alt="...">
            </div>
            <div class="col-md-6 offset-md-1">
              <div class="card-body">
                <h5 class="card-title">{userObject.firstname} {userObject.lastname}</h5>
                <p>Email : {userObject.email}</p>
                <p>Birthday : {userObject.birthday}</p>
                <p>Gender : {userObject.gender.upper()}</p>
                <p>Bio : {profileObject.bio}</p>
                <p>Nickname : {profileObject.nickname}</p>
                <p>Workplace : {profileObject.workplace}</p>
                <p>Skills : {profileObject.skills}</p>
                <p>University : {profileObject.university}</p>
                <p>School : {profileObject.school}</p>
                <p>Current City : {profileObject.current_city}</p>
                <p>Hometown : {profileObject.hometown}</p>
                <p>Other Places : {profileObject.other_places}</p>
                <p>Contact : {profileObject.contact}</p>
                <p>Relationship Status : {profileObject.relationship_status}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
  ''')


def createFriendsList():
    print('''
  <div class="container">
    <ul class="list-group list-group-flush">
    ''')


def createLi(friend):
    print(f'<li class="list-group-item">{friend}</li>')


def createFindFriendLi(friend, firstname, email):
    print(f'''<li class="list-group-item">
    {friend}
    <a href="friendsList.py?firstname={firstname}&email={email}&friend={friend}" class="addFriendBtn"><i class="fas fa-user-plus"></i></a>
    </li>''')


def endFriendsList():
    print('''</ul>
    </div>
    ''')


def createPostForm(firstname, email):
    print(f'''
    <div class="container">
        <div class="row">
            <div class="col-md-7 mt-5">
                <form action="login.py" method="POST" enctype="multipart/form-data">
                    <input type="hidden" name="firstname" value="{firstname}">
                    <input type="hidden" name="email" value="{email}">
                    <div class="form-group">
                        <label for="caption">Caption</label>
                        <input type="text" class="form-control" id="caption" name="caption" required>
                        <small class="form-text text-muted">Add some hashtags also !!</small>
                    </div>
                    <div class="form-group">
                        <label for="media">Add Media</label>
                        <input type="file" class="form-control" id="media" name="media">
                        <small class="form-text text-muted">Add jpg, png, or mp4 file..</small>
                    </div>
                    <button type="submit" class="btn btn-primary"
                        style="float: right; margin-left: 10px;">Submit</button>
                    <a href="login.py?firstname={firstname}&email={email}" style="float: right;" class="btn btn-outline-dark">Cancel</a>
                </form>
            </div>
        </div>
    </div>
    ''')


def newsFeedStart():
    print('''
    <div class="container">
    <br>
    <div class="row">
      <div class="col-md-7">
        <div class="row">
    ''')


def newsFeedPost(post):
  # firstname, post_time, caption, media_link, likes, comments, shares
    print(f'''
          <div class="col-md-12 mb-5">
            <div class="card" style="width: 100%; padding: 15px 25px 5px;">
              <h4 class="card-title" style="margin-bottom: 0; color: #3F9BAF"><i class="fas fa-user"></i>&nbsp;{post[0]}</h4>
              <p class="text-muted"><i class="fas fa-history"></i>&nbsp;&nbsp;{post[1]}</p>
              <p class="card-text">
                <pre>
                  {post[2]}
                </pre>
              </p>
              <div style="margin: auto;">
                <img src="../images/{post[3]}" class="card-img-top" alt="...">
              </div>
              <div class="card-body">
                <div class="row">
                  <div class="col-md-4">
                    <a href="#" class="btn btn-dark" style="width: 100%;"><i
                        class="fas fa-thumbs-up"></i>&nbsp;&nbsp;Like&nbsp;&nbsp;<span
                        class="badge badge-pill badge-light">{post[4]}</span></a>
                  </div>
                  <div class="col-md-4">
                    <a href="#" class="btn btn-dark" style="width: 100%;"><i
                        class="fas fa-comment-alt"></i>&nbsp;&nbsp;Comment&nbsp;&nbsp;<span
                        class="badge badge-pill badge-light">{post[5]}</span></a>
                  </div>
                  <div class="col-md-4">
                    <a href="#" class="btn btn-dark" style="width: 100%;"><i
                        class="fas fa-share"></i>&nbsp;&nbsp;Share&nbsp;&nbsp;<span
                        class="badge badge-pill badge-light">{post[6]}</span></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
    ''')


def newsFeedEnd():
    print('''        
        </div>
      </div>
      <div class="col-md-4 offset-md-1">
        <div class="row">
          <div class="col-md-12">
            <div class="card" style="width: 18rem; text-align: center;">
              <img src="https://i.udemycdn.com/course/240x135/1879018_95b6.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">NodeJS - The Complete Guide (incl. MVC, REST APIs, GraphQL)</h5>
                <p class="card-text">Master Node JS, build REST APIs with Node.js, GraphQL APIs, add Authentication, use
                  MongoDB, SQL & much more!</p>
                <a href="https://www.udemy.com/course/nodejs-the-complete-guide/" class="btn btn-outline-dark">Go to
                  course</a>
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <div class="card mt-2" style="width: 18rem; text-align: center;">
              <img src="https://i.udemycdn.com/course/240x135/857010_8239_2.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Learn Ethical Hacking From Scratch</h5>
                <p class="card-text">Become an ethical hacker that can hack computer systems like black hat hackers and
                  secure
                  them like security experts.</p>
                <a href="https://www.udemy.com/course/learn-ethical-hacking-from-scratch/"
                  class="btn btn-outline-dark">Buy
                  now</a>
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <div class="card mt-2" style="width: 18rem; text-align: center;">
              <img
                src="https://yt3.ggpht.com/kqNW98UOQclfO6CSZI2l60ss66VMyE1KhN34n2PhTQ_ioeg1X6w5Q7uiJ1gx_My_skPuSL8BLg=w1440-fcrop64=1,32b75a57cd48a5a8-k-c0xffffffff-no-nd-rj"
                class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Bret Fisher Docker and DevOps</h5>
                <p class="card-text">Focused on DevOps, containers, Docker, Kubernetes, and cloud, this channel me, Bret
                  Fisher, and my friends sharing and discussing topics for IT Pro's, Developers, Engineers, and
                  Sysadmins. Hopefully a bit more fun then what you're used to for "tech videos".</p>
                <a href="https://www.youtube.com/channel/UC0NErq0RhP51iXx64ZmyVfg/featured"
                  class="btn btn-outline-dark">Subscribe</a>
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <div class="card mt-2" style="width: 18rem; text-align: center;">
              <img src="https://i.ytimg.com/vi/FwvgeJn1de8/maxresdefault.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">21 Home Upgrades That You Can DIY for Under $50</h5>
                <p class="card-text">You don't need much cash to spruce up your property.</p>
                <a href="https://www.moneytalksnews.com/23-ways-make-your-house-look-awesome-for-50-less/?__cf_chl_captcha_tk__=23855f1a37ee7e1bcf93ec6ac79187cbcd32f2d5-1581520076-0-Af3ZKefmiYB_OPJkVZeTVctYDdccSIvqLy73DhTV3fiBvt8T82zqnGaODYPRBRirZ5Iogj_BrcMvV1DZd9JZezcfhX_8GN_Op5tnGNxDyKPcnr34_1DJ--aoDp20TXXKZkn-qV8QNCP2UGfSPI3lz45vN-m1ghwV80NbIMtsElC9urs7RxbS9IfFzAebvfeTud_QAT5nRiT2Qw4TUQQRs65DuE6ohBgq3ze6jfrOgGY458tgpJIAbkjHkdO4mOgGTvLRS8Vi--F6SiITnm3iL4tCqOhiPNMsJ5PLlGeSTr5dH4QwTxCBeZSFzznDhp28Yd9zf0Y3zCDY-YGF57AKwZVt2WnOhPbGq4LjOSJoc1GjLB3Mh6_zlu6BTQ1foYDARQ"
                  class="btn btn-outline-dark">Make
                  your home look great</a>
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <div class="card mt-2" style="width: 18rem; text-align: center;">
              <img src="http://farm1.static.flickr.com/101/296747958_8c15e91e3f_m.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">7 Essential Tips for Developing Skills</h5>
                <p class="card-text">Everyone wants to have a fulfilling career. But what do you think you need to have
                  it? </p>
                <a href="https://www.lifeoptimizer.org/2008/09/30/developing-skills/" class="btn btn-outline-dark">Here
                  are seven tips</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>
    ''')


def footer():
    print('''
    </body>
    </html>
  ''')
