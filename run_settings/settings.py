#!/usr/bin/env python
# Per-run settings of the experiments

import sys

def get_settings(name):
    # Return settings by name
    p = {}
    getattr(sys.modules[__name__], name)(p)
    return p

def base_settings(p):
    p['config'] = {}
    p['config']['HIT Configuration'] = {}
    p['exp'] = {}
    p['exp']['num_blocks'] = 6
    p['exp']['fixation_duration'] = 500
    p['exp']['presentation_duration'] = 100
    p['exp']['pretraining'] = 0
    p['exp']['training_presentation_durations'] = [500, 500, 200, 200, 100, 100]
    p['exp']['max_answer_times'] = [500, 500, 500, 500, 500, 500]
    p['exp']['trial_pretimes'] = [1100, 1200, 1300, 1400, 1500]
    p['exp']['max_training_answer_time'] = 1500
    p['exp']['answer_keys'] = [83, 76]
    p['exp']['answers'] = ['S', 'L']
    p['exp']['answer_strings'] = ['animal', 'non-animal']
    p['exp']['imagelist_identifiers'] = ['animal', 'nonanimal'] # Identifiers used in csv file
    p['exp']['example_stims'] = ["static/examples/ex1n.webm",
                          "static/examples/ex1a.webm",
                          "static/examples/ex2n.webm",
                          "static/examples/ex2a.webm",
                          "static/examples/ex3a.webm",
                          "static/examples/ex3n.webm"]
    p['exp']['example_stim_len'] = [1300, 1300, 1300, 1300, 1300, 1300]
    p['exp']['example_answers'] = [1, 0, 1, 0, 0, 1]
    p['exp']['example_pretime'] = 1100
    p['identifiers'] = {}
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> or <emph>non-animal</emph> image (including artificial and natural objects and scenes).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'non-animal'
    p['identifiers']['Class2'] = 'Non-animal'
    p['set_index'] = 70
    p['set_name'] = 'clicktionary'
    p['log_scale_revelations'] = False
    p['invert_revelations'] = True
    p['exclude_participants'] = []
    p['identifiers']['pay_amt'] = '1.50'
    p['identifiers']['exp_length'] = 15  # in minutes
    p['identifiers']['exp_title'] = p['identifiers']['Class1']+' or '+p['identifiers']['Class2']+'?'


def clicktionary(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_100'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(2000, 2020)
    p['config']['HIT Configuration']['title'] = 'Animal Realization'
    p['config']['HIT Configuration']['description'] = 'Categorize whether or not a scrambled image contains an animal'
    p['set_index'] = 50

def clicktionary50ms(p):
    base_settings(p)
    # Only set 1, 50ms presentation time, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_50'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(3000, 3020)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether or not a scrambled image contains an animal or a vehicle' # sic
    p['exp']['presentation_duration'] = 50

def clicktionary50msfull(p):
    base_settings(p)
    # Only set 1, 50ms presentation time, including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_50'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(4000, 4022)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 50

def clicktionary400msfull(p):
    base_settings(p)
    # Only set 1, 50ms presentation time, including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_400'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_masked_images_balanced_cut'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(4000, 4022)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400

def clicktionary400ms150msfull(p):
    base_settings(p)
    # Only set 1, 50ms presentation time, including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_400'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_masked_images_balanced_cut'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(4000, 4022)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['max_answer_times'] = [150, 150, 150, 150, 150, 150]

def clicktionary400msvaranswerfull(p):
    base_settings(p)
    # Only set 1, 50ms presentation time, including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_400'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_masked_images_balanced_cut'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(4000, 4022)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [100, 200, 300, 400, 500]
    p['exp']['pretraining'] = 1

def clicklog400ms150msfull(p):
    base_settings(p)
    # Only set 1, 50ms presentation time, including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_log_scale_masked_images_400'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_masked_images_balanced_cut'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['set_index'] = 80
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False

def clicklog400ms500msfull(p):
    clicklog400ms150msfull(p)
    # Only set 1, 400ms presentation time, including full revalation images, animal vs vehicle
    p['exp']['max_answer_times'] = [500] * p['exp']['num_blocks']
    p['desc'] = 'Set 1 log scale, Animal vs Vehicle, 400ms stim + 500ms answer'

def clickloglrp400ms500msfull(p):
    clicklog400ms150msfull(p)
    # Only set 1, 400ms presentation time, including full revalation images, animal vs vehicle
    p['exp']['max_answer_times'] = [500] * p['exp']['num_blocks']
    p['desc'] = 'Set 1 log scale, Animal vs Vehicle, 400ms stim + 500ms answer'

def charlie_test(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_masked_images_balanced_cut_100'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples'
    p['set_name'] = 'clicktionary'
    p['set_indices'] = range(2000, 2020)
    p['config']['HIT Configuration']['title'] = 'Animal Realization'
    p['config']['HIT Configuration']['description'] = 'Categorize whether or not a scrambled image contains an animal'
    p['set_index'] = 50
    p['exclude_participants'] = [
        'clicktionary',
        'clicktionary50ms',
        'clicktionary50msfull',
        'clicktionary400msfull',
        'clicktionary400ms150msfull',
        'clicktionary400msvaranswerfull']
    p['exclude_participants'] = ['clicklog400ms500msfull', 'clickloglrp400ms500msfull']

def click_probfill(p):
    base_settings(p)
    # Only set 1, 400ms presentation time + 500ms answer time including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_probabilistic_region_growth_400'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 100
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [500] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 500ms answer, probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicklog400ms500msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def click_center_probfill(p):
    base_settings(p)
    # Only set 1, 400ms presentation time + 500ms answer time including full revalation images, animal vs vehicle
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_centered_probabilistic_region_growth_50'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 50
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [500] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '50ms stim + 500ms answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull']
    p['cnn_class_file'] = 'classes_exp_1.txt'


def click_center_probfill_650(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_centered_probabilistic_region_growth_50'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 50
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [650] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '50ms stim + 650ms answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill']
    p['cnn_class_file'] = 'classes_exp_1.txt'


def lrp_center_probfill_650(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/lrp_centered_probabilistic_region_growth_50'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/lrp_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 130
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 50
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [650] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '50ms stim + 650ms answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def fixation_center_probfill_650(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/fixation_centered_probabilistic_region_growth_50'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/fixation_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 140
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 50
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [650] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '50ms stim + 650ms answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650']
    p['cnn_class_file'] = 'classes_exp_1.txt'



def click_center_probfill_400stim_300res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_centered_probabilistic_region_growth_400stim_300res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [300] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 300 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def lrp_center_probfill_400stim_300res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/lrp_center_probfill_400stim_300res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/lrp_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 130
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [300] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 300ms answer, lrp probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'fixation_center_probfill_400stim_300res']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def fixation_center_probfill_400stim_300res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/fixation_centered_probabilistic_region_growth_400stim_300res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/fixation_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 140
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [300] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 300ms answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def click_center_probfill_400stim_150res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/clicktionary_centered_probabilistic_region_growth_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'lrp_center_probfill_400stim_300res']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def lrp_center_probfill_400stim_150res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/lrp_centered_probabilistic_region_growth_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/lrp_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 130
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 150ms answer, lrp probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'lrp_center_probfill_400stim_300res',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res']
    p['cnn_class_file'] = 'classes_exp_1.txt'

def fixation_center_probfill_400stim_150res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/fixation_centered_probabilistic_region_growth_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/fixation_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 140
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 150ms answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res'
        ]
    p['cnn_class_file'] = 'classes_exp_1.txt'


def click_center_probfill_400stim_150res_2(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/click_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'


def click_center_probfill_400stim_150res_3(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/click_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'click_center_probfill_400stim_150res_2'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

def click_center_probfill_400stim_150res_4(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/click_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'


def click_center_probfill_400stim_150res_combined(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/click_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

def lrp_center_probfill_400stim_150res_2(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/lrp_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/lrp_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 130
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 150ms answer, lrp probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3',
        'click_center_probfill_400stim_150res_4'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

def lrp_center_probfill_400stim_150res_combined(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/lrp_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/lrp_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 130
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400ms stim + 150ms answer, lrp probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3',
        'click_center_probfill_400stim_150res_4'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

def click_center_probfill_400stim_150res_5(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/click_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3',
        'click_center_probfill_400stim_150res_4'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

# TURK experiment by Michele and Charlie 2017 May
def artifact_vehicles_turk(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/artifact_vehicles_turk_50ms'
    p['input_image_path'] = '/media/data_cifs/nsf_levels/michele/entire_sets/artifact_testing_set_for_humans/artifact_testing_set/'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/artifact_vehicles_examples'
    p['set_name'] = 'artifact_vehicles_turk'
    p['set_index'] = 0
    p['set_indices'] = [0]
    p['exp']['answer_strings'] = ['non vehicle', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains a <emph>vehicle</emph> (airplane, truck, car, boat, bicycle, etc.) or <emph>does not contain a vehicle</emph> (building, clothing, electronic device, etc.).'
    p['identifiers']['class1'] = 'non vehicle'
    p['identifiers']['Class1'] = 'Non vehicle'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['identifiers']['pay_amt'] = '2.00'
    p['identifiers']['exp_length'] = 22 # in minutes
    p['identifiers']['exp_title'] = 'Vehicle or Not?'
    p['config']['HIT Configuration']['title'] = p['identifiers']['exp_title']
    p['config']['HIT Configuration']['description'] = 'Categorize whether an image contains a vehicle or does not contain a vehicle.'
    p['exp']['presentation_duration'] = 50 # ms
    p['exp']['num_blocks'] = 6
    p['exp']['max_answer_times'] = [500] * p['exp']['num_blocks']
    p['exp']['imagelist_identifiers'] = ['distractor', 'target']  # Identifiers used in csv file
    # p['exp']['pretraining'] = 0
    # p['log_scale_revelations'] = True
    # p['invert_revelations'] = False
    # p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = []
    # p['cnn_class_file'] = 'classes_exp_1.txt'

def lrp_center_probfill_400stim_150res_3(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/lrp_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/lrp_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 130
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, lrp probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3',
        'click_center_probfill_400stim_150res_4',
        'click_center_probfill_400stim_150res_5'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

def bubbles_center_probfill_400stim_150res(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/bubbles_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/bubbles_probabilistic_region_growth_centered'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'vehicle']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (dog, cat, fish, etc.) or a <emph>vehicle</emph> (airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'vehicle'
    p['identifiers']['Class2'] = 'Vehicle'
    p['config']['HIT Configuration']['title'] = 'Animal or Vehicle?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether a scrambled image contains an animal or a vehicle'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, bubbles probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3',
        'click_center_probfill_400stim_150res_4',
        'click_center_probfill_400stim_150res_5',
        'lrp_center_probfill_400stim_150res_3'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

def click_center_probfill_400stim_150_animal_nonanimal(p):
    base_settings(p)
    p['video_base_path'] = '/media/data_clicktionary/rapid_categorization/click_center_probfill_400stim_150res'
    p['input_image_path'] = '/media/data_cifs/clicktionary/causal_experiment/clicktionary_centered_probabilistic_region_growth'
    p['example_path'] = '/media/data_clicktionary/rapid_categorization/masked_examples_animal_vehicle'
    p['set_name'] = 'clicktionary'
    p['set_index'] = 120
    p['set_indices'] = range(5000, 5024)
    p['exp']['answer_strings'] = ['animal', 'nonanimal']
    p['identifiers']['taskexpl'] = 'Your task will be to assess whether the pictured photograph contains an <emph>animal</emph> (for example a dog, cat, fish, etc.) or <emph>not</emph> (for example an airplane, truck, car, boat, etc.).'
    p['identifiers']['class1'] = 'animal'
    p['identifiers']['Class1'] = 'Animal'
    p['identifiers']['class2'] = 'non-animal'
    p['identifiers']['Class2'] = 'Non-animal'
    p['config']['HIT Configuration']['title'] = 'Animal or not an animal?'
    p['config']['HIT Configuration']['description'] = 'Categorize whether or not a scrambled image contains an animal'
    p['exp']['presentation_duration'] = 400
    p['exp']['num_blocks'] = 5
    p['exp']['max_answer_times'] = [150] * p['exp']['num_blocks']
    p['exp']['pretraining'] = 0
    p['log_scale_revelations'] = True
    p['invert_revelations'] = False
    p['desc'] = '400 stim + 150 answer, centered probabilistic revelation'
    p['exclude_participants'] = [
        'clicklog400ms150msfull',
        'clicktionary',
        'clicktionary400ms150msfull',
        'clicktionary400msfull',
        'clicktionary400msvaranswerfull',
        'clicktionary50ms',
        'clicktionary50msfull',
        'click_center_probfill',
        'click_center_probfill_650',
        'lrp_center_probfill_650',
        'fixation_center_probfill_400stim_300res',
        'click_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res',
        'lrp_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_2',
        'click_center_probfill_400stim_150res_3',
        'click_center_probfill_400stim_150res_4',
        'lrp_center_probfill_400stim_150res_3'
    ]
    p['cnn_class_file'] = 'classes_exp_1.txt'

