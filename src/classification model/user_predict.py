import pandas as pd
import joblib
import os


MODEL_DIR = 'spotify-jrock-eurock/models/'  


def load_model():
    model_path = os.path.join(MODEL_DIR, 'region_classifier_model.pkl')
    encoder_path = os.path.join(MODEL_DIR, 'region_label_encoder.pkl')
    
    if os.path.exists(model_path) and os.path.exists(encoder_path):
        model = joblib.load(model_path)
        le = joblib.load(encoder_path)
        return model, le
    else:
        print(f"Model files not found in directory {MODEL_DIR}")
        return None, None
    

def get_user_features(features):
    user_input = {}
    
    print("\nEnter values ​​for the following attributes (from 0 to 1, for tempo from 50 to 200, for duration from 120000 to 300000):")
    
    for feature in features:
        valid_input = False
        while not valid_input:
            try:
                if feature == 'Tempo':
                    value = float(input(f"{feature} (50-200): "))
                    if 50 <= value <= 200:
                        valid_input = True
                    else:
                        print("The value must be between 50 and 200.")
                elif feature == 'Duration':
                    value = float(input(f"{feature} (120000-300000 milliseconds): "))
                    if 120000 <= value <= 300000:
                        valid_input = True
                    else:
                        print("The value should be from 120000 to 300000 milliseconds (2-5 minutes).")
                elif feature == 'Loudness':
                    value = float(input(f"{feature} (-60 and 0 dB): "))
                    if -60 <= value <= 0:
                        valid_input = True
                    else:
                        print("The value must be between -60 and 0.")
                elif feature == 'Popularity':
                    value = float(input(f"{feature} (0-100): "))
                    if 0 <= value <= 100:
                        valid_input = True
                    else:
                        print("The value must be between 0 and 100.")
                else:
                    value = float(input(f"{feature} (0-1): "))
                    if 0 <= value <= 1:
                        valid_input = True
                    else:
                        print("The value must be between 0 and 1.")
                user_input[feature] = value
            except ValueError:
                print("Please enter a numeric value.")
    
    return user_input


def predict_region(model, le, user_input, features):

    input_df = pd.DataFrame([user_input])
    input_df = input_df[features]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    predicted_region = le.inverse_transform([prediction])[0]

    print(f"\nForecasted region: {predicted_region}")

    for i, region in enumerate(le.classes_):
        print(f"Probability for {region}: {probability[i]:.2f} ({probability[i]*100:.1f}%)")
    
    return predicted_region, probability

def main():

    features = [
        'Popularity', 'Duration', 'Acousticness', 'Danceability', 'Energy',
        'Instrumentalness', 'Liveness', 'Loudness', 'Speechiness', 'Tempo', 'Valence'
    ]

    model, le = load_model()
    
    if model is None or le is None:
        print("To use the script, you must first train the model.")
        print("Make sure the model and encoder are saved as 'region_classifier_model.pkl' and 'region_label_encoder.pkl'")

    print("\nWelcome to the Music Classification by Region (Europe/Japan) program")
    print("Enter track characteristics for region prediction")
    
    while True:
        user_input = get_user_features(features)

        predict_region(model, le, user_input, features)
        
        continue_choice = input("\nWould you like to classify another track? (yes/no): ").lower()
        if continue_choice != 'yes' and continue_choice != 'y' and continue_choice != 'Yes':
            break
    
    print("Thank you for using the music classification program!")

if __name__ == "__main__":
    main()