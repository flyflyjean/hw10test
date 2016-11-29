try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command
    
setup(
        name="CalCalc",
        version= "0.0.1",
        description="'calculate' that evaluates any string passed to it",
        author="Jing Dai",
        author_email="jdai@berkeley.edu",
        url="https://github.com/flyflyjean/JingDai_AY250_HW10.git",
        license = 'None',
        packages=['calcalc'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
)
