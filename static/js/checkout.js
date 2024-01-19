$(document).ready(function (){
    $('.payWithRazorpay').click(function(e){
        e.preventDefault();
        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var pincode = $("[name='pincode']").val();
        var token = $("[name= 'csrfmiddlewaretoken']").val();

        if(fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == "" || country == "" || pincode == "" )
        {
            swal("Alert!" ,"All fields are mandatory!","error");
            return false;
        }
        else
        {
            $.ajax({     
                method:"GET",
                url:"/proceed-to-pay",
                success: function (response){ 
                    // console.log(response);
                    var options = {
                        "key": "rzp_test_6jcn81y2q8hZnc", // Enter the Key ID generated from the Dashboard
                        "amount":response.total_price, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise or INR 500.
                        "currency": "INR",
                        // client = razorpay.Client(auth=('rzp_test_6jcn81y2q8hZnc','FZPFBXg5EofMkgh4rXzn93b6')),

                        "name": "Al Hajima Syed Ali",
                        "description": "Thank you for buying from us.",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm",//This is a sample Order ID. Create an Order using Orders API. (https://razorpay.com/docs/payment-gateway/orders/integration/#step-1-create-an-order). Refer the Checkout form table given below
                        "handler": function (response){
                            alert(response.razorpay_payment_id);
                            data = {
                                "fname":fname,
                                "lname":lname,
                                "email":email,
                                "phone": phone,
                                "address":address,
                                "city":city,
                                "state":state,
                                "country":country,
                                "pincode":pincode,
                                "payment_mode": "Paid by Razprpay",
                                "payment_id": "response.razorpay_payment_id",
                                csrfmiddlewaretoken: token 
     
        
                            }
                            $.ajax({
                                method: "POST",
                                url: "/place-order",
                                data: data,
                                success: function(responsec){
                                    swal("Congratulations!",responsec.status,"success").then((value) => {
                                        window.location.href = '/my-orders'

                                    });
                                } 
                            });

                            
                        },
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact":phone
                        },
                       
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();

                }


            });
            
          
                           
       


            
           
     
        }
    });

 
});
