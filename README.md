# IASEP Medical Services Guide
![Medical Services Guide](https://raw.githubusercontent.com/marcelofa/deadlines_app/master/banner.png)

This is a small medical services guide project intended to provide better user experience than the [standard guide](http://www.e-saude.iasep.pa.gov.br/servicos) from the state goverment.


## Install Required Packages

This project requires a few packages. To install them use the following command:

    pip install -r requirements.txt


## Running the Application

Before running the application we need to create the needed DB tables and run some migrations:

    manage.py migrate

Now you can run the development web server:

    manage.py runserver
    
To access the application go <http://localhost:8000/>


## License

This project is licensed under the  GNU Version 3 License - see the [LICENSE.md](LICENSE.md) file for details
