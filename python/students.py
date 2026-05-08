from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
def App():
    put_html('<center><h3>مرحبا في سنتر مستر عمرو الشبراوي </h3></center>').style('background-color:#25316D; color:gold; padding:25px;')
    put_html('<p> تطبيق تنظيم الطلاب</p>').style('text-align:center; font-wieght:bold;')
    put_html('<cnter><img src="https://www.tvdsb.ca/en/schools/resources/Information-for-Grade-8-students/Info-for-Grade-8-banner.jpg"></center>')
    data= input_group(
        'ملئ بيانات الطالب',
        [
            input('اسم الطالب ' , name='student'),
            input('مجموعة الطالب' , name='numbers'),
            input('رقم الطالب ف المجموعة' , name='groubnumber'),
            input('رقم الطالب' , name='phones', type=NUMBER),
            input('رقم ولي الامر' , name='phdorm', type=NUMBER),
            radio('الصف الدراسي' , options= ['اولى ثانوي/بكلوريا','تالتة ثانوي'], name='certi')
        ]
    )
    put_text('student cv')
    put_table([
        ['student','numbers','groubnumber','phones','phdorm','certi'],
        [data['student'],data['numbers'],data['groubnumber'],data['phones'],data['phdorm'],data['certi']]
    ])
start_server(App , port=3333 , debug=True) 
