def header(heading):
    print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <a class="navbar-brand" href="home.py">OnlineShop</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="nav-link" href="#">Login & Signup <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="cart.py">My Cart</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Categories
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="home.py?category=men's fashion">Men</a>
                <a class="dropdown-item" href="home.py?category=women's fashion">Women</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="home.py?category=electronics">Electronics</a>
              </div>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0" action="search.py">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" name="q">
            <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </nav>
      <div class="container">
        <h1 class="text-center">{heading}</h1>
        <hr>

      <div class="row">''')

def createProduct(product):
    print(f'''      
      <div class="col-xl-4 col-md-6">
      <div class="card" style="width: 18rem; height:35rem; margin-bottom: 25px;">
        <div class="{product['product_sub_category']}-parent">
          <img src="{product['product_image']}" class="card-img-top {product['product_sub_category']}" alt="...">
        </div>
        <div class="card-body">
          <h5 class="card-title">{product['product_brand']} {product['product_name']}</h5>
          <p class="card-text">&#8377;{product['product_price']}</p>
          <a href="view_product.py?pid={product['product_id']}" class="btn btn-primary">View Product</a>
        </div>
      </div>
    </div>
    ''')

def createHorizontalProduct(product):
  print(f'''
    <div class="card mb-3" style="width:100%;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img src="{product['product_image']}" class="card-img" id="horizontalProduct"  alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{product["product_brand"]} {product['product_name']}</h5>
        <p class="card-text">&#8377;{product['product_price']}</p>
        <p class="card-text"><small class="text-muted">{product['discount_percentage']}% off</small></p>
        <a href="cart.py?pid={product['product_id']}" class="btn btn-primary">Add To Cart</a>
      </div>
    </div>
  </div>
</div>
  ''')

def footer():
    print('''</div>
    </div>
</body>
</html>
''')