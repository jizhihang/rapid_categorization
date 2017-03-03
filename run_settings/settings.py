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
