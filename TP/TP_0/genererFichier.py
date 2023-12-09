import random

def generate_point_cloud(num_points, noise_factor):
    points = []
    for _ in range(num_points):
        x = random.uniform(0, 0.05)  # Exemple : valeurs entre 0 et 100
        y = random.uniform(0, 0.05)
        z = random.uniform(0, 0.05)

        # Ajout de bruit (ajusté pour être plus proche)
        x += random.uniform(-noise_factor / 10, noise_factor / 10)
        y += random.uniform(-noise_factor / 10, noise_factor / 10)
        z += random.uniform(-noise_factor / 10, noise_factor / 10)

        points.append((x, y, z))

    return points

def save_point_cloud_to_file(points, filename):
    with open(filename, 'w') as file:
        for point in points:
            file.write(f"{point[0]}\t{point[1]}\t{point[2]}\n")

if __name__ == "__main__":
    num_points_to_generate = 10000
    noise_factor = 1  # Ajustez cela en fonction du niveau de bruit souhaité
    output_filename = "nuage_point.txt"

    point_cloud = generate_point_cloud(num_points_to_generate, noise_factor)
    save_point_cloud_to_file(point_cloud, output_filename)

    print(f"Nuage de points généré et enregistré dans {output_filename}")

