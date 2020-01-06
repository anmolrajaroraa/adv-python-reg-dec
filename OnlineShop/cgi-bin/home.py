#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-type: text/html\r\n\r\n")

products = [{
            "product_id" : 1,
            "product_brand" : "Realme",
            "product_name" : "C2 (Diamond Blue, 32 GB)",
            "product_image" : "https://rukminim1.flixcart.com/image/312/312/k0lbdzk0pkrrdj/mobile-refurbished/z/j/2/c2-16-u-rmx1945-realme-2-original-imaffnumygt8wgfx.jpeg?q=70",
            "product_price" : 6499,
            "product_mrp" : 7999,
            "discount_percentage" : 18,
            "product_rating" : 4.4,
            "product_category" : "mobiles"
        },
        {
            "product_id" : 2,
            "product_brand" : "Realme",
            "product_name" : "XT (Pearl Blue, 64 GB)",
            "product_image" : "https://rukminim1.flixcart.com/image/312/312/k2jbyq80pkrrdj/mobile-refurbished/e/s/v/xt-128-a-rmx1921-realme-8-original-imafk8h2gbyatyyr.jpeg?q=70",
            "product_price" : 15999,
            "product_mrp" : 16999,
            "discount_percentage" : 5,
            "product_rating" : 4.5,
            "product_category" : "mobiles"
        },
        {
            "product_id" : 3,
            "product_brand" : "Realme",
            "product_name" : "5 (Crystal Blue, 32 GB)",
            "product_image" : "https://rukminim1.flixcart.com/image/312/312/k2jbyq80pkrrdj/mobile-refurbished/q/m/g/5-64-c-rmx1911-realme-4-original-imafje89tgyzdj7c.jpeg?q=70",
            "product_price" : 8999,
            "product_mrp" : 10999,
            "discount_percentage" : 18,
            "product_rating" : 4.5,
            "product_category" : "mobiles"
        },
        {
            "product_id" : 4,
            "product_brand" : "Realme",
            "product_name" : "5 Pro (Crystal Green, 64 GB)",
            "product_image" : "https://rukminim1.flixcart.com/image/312/312/k2jbyq80pkrrdj/mobile-refurbished/n/y/f/5-pro-64-u-rmx1971-realme-4-original-imafjhk3dyggb2bg.jpeg?q=70",
            "product_price" : 13999,
            "product_mrp" : 14999,
            "discount_percentage" : 6,
            "product_rating" : 4.5,
            "product_category" : "mobiles"
        },
        {
            "product_id" : 5,
            "product_brand" : "iFFALCON by TCL",
            "product_name" : "AI Powered K31 138.78cm (55 inch) Ultra HD (4K) LED Smart Android TV with HDR 10  (55K31)",
            "product_image" : "https://rukminim1.flixcart.com/image/416/416/k2w6xe80/television/v/5/7/iffalcon-55k31-original-imafm59fa7ftgpkm.jpeg?q=70",
            "product_price" : 29999,
            "product_mrp" : 70990,
            "discount_percentage" : 57,
            "product_rating" : 4.4,
            "product_category" : "televisions"
        },
        {
            "product_id" : 6,
            "product_brand" : "Vu",
            "product_name" : "Pixelight 108cm (43 inch) Ultra HD (4K) LED Smart TV with Cricket Mode  (43-UH)",
            "product_image" : "https://rukminim1.flixcart.com/image/416/416/k1nw9zk0/television/t/a/x/vu-43-uh-43-uh-original-imafh4jgug563fyw.jpeg?q=70",
            "product_price" : 22499,
            "product_mrp" : 36000,
            "discount_percentage" : 37,
            "product_rating" : 4.4,
            "product_category" : "televisions"
        },
        {
            "product_id" : 7,
            "product_brand" : "Samsung",
            "product_name" : "192 L Direct Cool Single Door 5 Star Refrigerator with Base Drawer  (Saffron Blue, RR20R182XU8/HL)",
            "product_image" : "https://rukminim1.flixcart.com/image/416/416/jr0y9ow0/refrigerator-new/r/k/j/rr20r182xu8-hl-5-samsung-original-imafcp6v6hgqztkg.jpeg?q=70",
            "product_price" : 15790,
            "product_mrp" : 20400,
            "discount_percentage" : 22,
            "product_rating" : 4.5,
            "product_category" : "refrigerators"
        },
        {
            "product_id" : 8,
            "product_brand" : "Samsung",
            "product_name" : "6.2 kg ActivWash+ Fully Automatic Top Load Grey  (WA62N4422BS/TL)",
            "product_image" : "https://rukminim1.flixcart.com/image/416/416/jtuej680/washing-machine-new/s/q/f/wa62n4422bs-tl-samsung-original-imaff2sfeukwvrhm.jpeg?q=70",
            "product_price" : 15300,
            "product_mrp" : 19890,
            "discount_percentage" : 23,
            "product_rating" : 4.4,
            "product_category" : "washing-machines"
        },
        {
            "product_id" : 9,
            "product_brand" : "Butterfly",
            "product_name" : "Rapid 4 Jar 750 watts 750 W Juicer Mixer Grinder",
            "product_image" : "https://rukminim1.flixcart.com/image/612/612/jmi22kw0/mixer-grinder-juicer/n/z/a/butterfly-rapid-4-jar-750-watts-original-imaf5dvgugcqyug3.jpeg?q=70",
            "product_price" : 2849,
            "product_mrp" : 5499,
            "discount_percentage" : 48,
            "product_rating" : 4.1,
            "product_category" : "home-kitchen"
        },
        {
            "product_id" : 10,
            "product_brand" : "Prestige",
            "product_name" : "Atlas Plus 750 W Juicer Mixer Grinder",
            "product_image" : "https://rukminim1.flixcart.com/image/612/612/jyrl4sw0/mixer-grinder-juicer/z/d/j/prestige-41386-original-imafgxhgfvsgrrf4.jpeg?q=70",
            "product_price" : 2799,
            "product_mrp" : 4995,
            "discount_percentage" : 43,
            "product_rating" : 4.3,
            "product_category" : "home-kitchen"
        },
        {
            "product_id" : 11,
            "product_brand" : "Flipkart Smartbuy",
            "product_name" : "Tornado 750 W Mixer Grinder",
            "product_image" : "https://rukminim1.flixcart.com/image/612/612/jksm4y80/mixer-grinder-juicer/5/j/d/flipkart-smartbuy-fksbmg750su-original-imaf82g9azxspyfd.jpeg?q=70",
            "product_price" : 1999,
            "product_mrp" : 3899,
            "discount_percentage" : 48,
            "product_rating" : 4.2,
            "product_category" : "home-kitchen-big"
        },
        {
            "product_id" : 12,
            "product_brand" : "Billion",
            "product_name" : "MG91 Power Grind 750 W Mixer Grinder",
            "product_image" : "https://rukminim1.flixcart.com/image/612/612/j5tx4sw0-1/mixer-grinder-juicer/u/h/h/billion-powergrind-original-imaewfjncx8t2baz.jpeg?q=70",
            "product_price" : 1849,
            "product_mrp" : 3199,
            "discount_percentage" : 42,
            "product_rating" : 4.1,
            "product_category" : "home-kitchen-big"
        },
        {
            "product_id" : 13,
            "product_brand" : "Fastrack",
            "product_name" : "68007PP01 Trendies Analog Watch - For Women",
            "product_image" : "https://rukminim1.flixcart.com/image/880/1056/jiklh8w0/watch/x/g/4/68007pp01-fastrack-original-imaf6cffjkmtzahb.jpeg?q=50",
            "product_price" : 1271,
            "product_mrp" : 1695,
            "discount_percentage" : 25,
            "product_rating" : 4.3,
            "product_category" : "watches"
        },
        {
            "product_id" : 14,
            "product_brand" : "Sonata",
            "product_name" : "77106SM04 Analog Watch - For Men",
            "product_image" : "https://rukminim1.flixcart.com/image/880/1056/k0o69ow0/watch/f/g/c/77106sm04-sonata-original-imafkf7uhcfvndcv.jpeg?q=50",
            "product_price" : 999,
            "product_mrp" : 1249,
            "discount_percentage" : 20,
            "product_rating" : 4.4,
            "product_category" : "watches"
        },
        {
            "product_id" : 15,
            "product_brand" : "Daniel Klein",
            "product_name" : "DK11421-7 Analog Watch - For Women",
            "product_image" : "https://rukminim1.flixcart.com/image/880/1056/j44h7680/watch/g/d/d/dk11421-7-daniel-klein-original-imaev3qfcd8uf8na.jpeg?q=50",
            "product_price" : 1599,
            "product_mrp" : 3750,
            "discount_percentage" : 57,
            "product_rating" : 4.4,
            "product_category" : "watches"
        }
    ]

print('''
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
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <a class="navbar-brand" href="#">OnlineShop</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="nav-link" href="#">Login & Signup <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">My Cart</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Categories
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Men</a>
                <a class="dropdown-item" href="#">Women</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Electronics</a>
              </div>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </nav>
      <div class="container">
        <h1 class="text-center">Products</h1>
        <hr>

      <div class="row">''')

for product in products:
    print(f'''      
      <div class="col-xl-4">
      <div class="card" style="width: 18rem; margin-bottom: 25px;">
        <img src="{product['product_image']}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{product['product_brand']} {product['product_name']}</h5>
          <p class="card-text">&#8377;{product['product_price']}</p>
          <a href="#" class="btn btn-primary">View Product</a>
        </div>
      </div>
    </div>
    ''')

print('''</div>
    </div>
</body>
</html>
''')