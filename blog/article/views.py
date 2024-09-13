from django.shortcuts import render
from .models import Topic,Atricle
from . import forms

# Create your views here.


def send_input_data(request):

  form = forms.InputForm()
  
  if request.method == "POST":
      
      form = forms.InputForm(request.POST)
      
      if form.is_valid():
          print("Valid!!!")
      else:
              
          print("Invalid")
              
           
  
  return render(request,'input.html',{'form':form})
  
  
def show_topics(request):

  topics = Topic.objects.all()
  
  return render(request,'index.html',{'topics':topics})


def showarticle(request):

    title = "FIRST ARTICLE"
    author = "Gugu"
    article_text = """
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas viverra neque tincidunt risus consequat, sit amet interdum urna fermentum. Proin sagittis nulla sed vulputate gravida. Quisque tristique suscipit ante viverra ultricies. Morbi at consectetur nibh, vulputate pretium neque. Phasellus sodales sit amet justo quis porttitor. Vivamus fermentum faucibus porttitor. Aenean augue massa, dictum feugiat pretium semper, malesuada eget ligula. Quisque eleifend rutrum semper. Sed eget nulla at nisl iaculis elementum quis ac orci. Duis ullamcorper ultricies mi, id venenatis lectus tristique eu. Praesent varius sed massa ut scelerisque. Curabitur ornare vehicula orci tristique aliquet. Quisque et suscipit ex.

 Sed tincidunt nisi in nibh ultricies sollicitudin. Praesent pharetra, sem id tempus accumsan, velit purus mattis ipsum, quis laoreet augue odio in sem. Aliquam aliquam tellus sed erat laoreet, ut mollis mi vestibulum. In sodales a massa consectetur volutpat. Fusce vestibulum, risus eget maximus imperdiet, tellus lorem consectetur dui, eu facilisis quam ex nec augue. Donec dapibus erat non hendrerit condimentum. Praesent ultricies condimentum tellus, ac vehicula dui iaculis nec. Aenean quis diam sollicitudin, accumsan ipsum quis, sagittis quam. In hac habitasse platea dictumst. Nulla quis augue vestibulum, convallis tortor mollis, tincidunt lectus. Donec venenatis, ante a euismod sagittis, enim ante auctor leo, cursus tristique enim tortor vitae tortor. Nulla dignissim feugiat dui, ut egestas ipsum malesuada eget.

 Vestibulum turpis sem, faucibus in metus in, gravida cursus diam. Duis feugiat tellus vitae ex molestie, in convallis erat bibendum. Suspendisse tincidunt odio eu auctor vehicula. Donec bibendum odio quis facilisis molestie. Aenean laoreet sit amet dui ut molestie. Morbi rhoncus sem ligula, nec consectetur ex luctus ac. Praesent convallis diam eget vulputate placerat. Sed vel urna sagittis, euismod purus at, fermentum erat. Donec viverra libero in metus venenatis, quis euismod ante blandit. Suspendisse potenti. Aliquam erat volutpat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam fringilla, ex vestibulum mattis pharetra, lacus turpis gravida ipsum, in vulputate elit libero ac arcu. Nunc volutpat eros id sapien varius viverra.

 Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur velit ex, euismod vel metus imperdiet, mattis aliquet sapien. Nam vel leo odio. Fusce feugiat, dui non vehicula scelerisque, dui velit elementum sem, vulputate finibus dui diam at mauris. Phasellus ac dictum risus, a scelerisque eros. Aenean porttitor molestie pellentesque. Pellentesque dui justo, dapibus vel molestie at, ultrices ac neque. Nulla facilisi. Aliquam molestie, leo in accumsan fermentum, dui nisi commodo diam, vel molestie est metus a est. Cras at dignissim neque.

 Aenean purus lectus, mollis sit amet risus at, ultricies rhoncus leo. Curabitur enim lacus, porttitor non purus at, cursus condimentum nibh. Nullam lacus ligula, viverra ut eleifend commodo, ornare in nunc. In hac habitasse platea dictumst. Sed lacinia et tortor at cursus. Aliquam erat volutpat. Pellentesque eget ligula felis. Etiam purus urna, pulvinar eu lorem nec, vestibulum vehicula velit. Praesent convallis nunc lorem, id consequat felis egestas id. In tristique massa sed neque scelerisque molestie.

 Ut lobortis nulla ut justo placerat rutrum. Quisque in nunc imperdiet, tempor tellus ut, sodales sapien. Nulla ornare blandit dolor sit amet volutpat. Mauris et rutrum nisl. Morbi vulputate semper vehicula. Etiam non mi felis. Proin ultrices lacus at nibh iaculis, id consectetur ligula aliquam. Pellentesque a tempus justo. Fusce et turpis vitae nulla feugiat bibendum. Ut pretium convallis odio, et sollicitudin enim vestibulum vitae.que faucibus efficitur ex, et ultrices mi rutrum eu. Curabitur eu pulvinar dolor, in dictum lectus. Nulla malesuada est mi, ac vulputate leo feugiat tincidunt. Curabitur vitae semper elit, sit amet eleifend neque. In vel lorem at tortor lacinia consequat ut at est. Sed semper vulputate mollis. Proin sodales pellentesque risus, et finibus arcu rhoncus in. Praesent rutrum ante et lacus consequat congue. Aenean ornare posuere nibh.
 """
    return render(request,'article/article.html',{'title':title,'author':author,'article_text':article_text})
