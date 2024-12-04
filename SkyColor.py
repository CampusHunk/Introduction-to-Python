"""
Why is the Sky Blue? - A Scientific Explanation through Python
"""

def demonstrate_rayleigh_scattering():
    # Wavelengths of different colors of light (in nanometers)
    light_wavelengths = {
        'violet': 380,
        'blue': 450,
        'green': 530,
        'yellow': 580,
        'red': 700
    }
    
    print("Understanding why the sky is blue:\n")
    print("1. Sunlight contains all colors of visible light.")
    print("2. As light travels through the atmosphere, it collides with gas molecules.")
    print("3. These molecules scatter different wavelengths of light differently.\n")
    
    # Demonstrate Rayleigh scattering formula (scattered intensity ∝ 1/wavelength⁴)
    print("Relative scattering intensity for different colors:")
    for color, wavelength in light_wavelengths.items():
        # Calculate relative scattering (normalized to red light)
        scattering = ((700/wavelength)**4)
        bars = int(scattering * 5)  # Scale for visualization
        print(f"{color.capitalize():8} {'|' * bars} ({scattering:.1f}x)")
    
    print("\nConclusion:")
    print("- Blue light (wavelength ~450nm) is scattered about 5.7 times more than red light (700nm)")
    print("- This stronger scattering of blue light by air molecules makes the sky appear blue")
    print("- During sunrise/sunset, sunlight travels through more atmosphere,")
    print("  most blue light gets scattered away, leaving mainly red light to reach our eyes")

if __name__ == "__main__":
    demonstrate_rayleigh_scattering()
