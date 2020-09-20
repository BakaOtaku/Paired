<p align="center"><img src="https://image.flaticon.com/icons/svg/2036/2036962.svg" align="center" width="175"></p>
<h1 align="center">Paired</h1>

> An app that makes communication with the deaf and dumb smart by converting their hand gestures to text which can be understood by normal person.

### Motive

For actions to speak louder than words Actum has been designed to enhance the communication between normal and specially abled (deaf and dumb).

### Technologies

- Django
- Image Processing
- Image classfication using classifier
- Image classification using CNN classifier
- CNN classifier build using Tensorflow

### Testing

<img src="sample.png" width="200">


### offline setup and run

move to project root-  paired


1. Create and activate a virtualenv (Python 3)
```bash
python -m venv myenv
cd myenv/Scripts
source activate
cd ../..
```
2. Install requirements
```bash
pip install django
pip install imageio
pip install tensorflow
pip install scikit-image
pip install cv2
pip install numpy
```
3. move to backend
```
move to pairedBackend directory

```
4. Start database Server
```
python manage.py makemigrations
python manage.py migrate

```


5. Create admin user
```bash
./manage.py createsuperuser (not mandatory)
enter name ,email,password ,confirm password,and press y
```

6. Run development server
```bash
./manage.py runserver
```

7. live
http://127.0.0.1:8000/home/


