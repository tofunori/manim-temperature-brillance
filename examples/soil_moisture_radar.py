from manim import *
import numpy as np

"""
Animation sur l'humidité du sol avec radar
Cette animation vise à expliquer la relation entre la rugosité du sol, l'humidité et
le coefficient de rétrodiffusion radar, ainsi que l'influence de l'angle d'incidence.
"""

# Définition des constantes et paramètres
LOW_ROUGHNESS_Ks = 0.4
HIGH_ROUGHNESS_Ks = 1.2
DRY_SOIL_DIELECTRIC = 4
WET_SOIL_DIELECTRIC = 20


class RadarBasics(Scene):
    """
    Cette classe présente les concepts de base de la télédétection radar
    """
    def construct(self):
        # Titre
        title = Text("Principes de la télédétection radar", font_size=42)
        subtitle = Text("Mesure de l'humidité du sol", font_size=32, color=BLUE)
        subtitle.next_to(title, DOWN)
        
        # Animation du titre
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)
        
        # Déplacer le titre vers le haut
        self.play(
            title.animate.scale(0.6).to_edge(UP, buff=0.2),
            subtitle.animate.scale(0.6).next_to(title, DOWN, buff=0.1),
            run_time=1
        )
        
        # Principe de base du radar
        radar_principle = Text("Comment fonctionne un radar?", font_size=32, color=YELLOW)
        radar_principle.next_to(subtitle, DOWN, buff=0.7)
        
        # Animation du principe radar
        self.play(Write(radar_principle), run_time=1)
        
        # Créer un schéma simple du principe radar
        # Créer la surface et le radar
        radar = Circle(radius=0.3, color=WHITE)
        radar.set_fill(GRAY, opacity=0.5)
        radar.move_to(UP * 2 + LEFT * 4)
        
        radar_dish = Arc(radius=0.5, angle=PI/2, color=WHITE)
        radar_dish.next_to(radar, RIGHT, buff=-0.5)
        
        # Surface du sol
        ground = Line(LEFT * 7, RIGHT * 7, color=BROWN)
        ground.move_to(DOWN * 2)
        
        # Onde radar
        radar_wave_out = DashedLine(radar.get_center(), ground.point_from_proportion(0.7), color=YELLOW)
        radar_wave_back = DashedLine(ground.point_from_proportion(0.7), radar.get_center(), color=RED)
        
        # Ajouter des étiquettes
        emitted_label = Text("Signal émis", font_size=20, color=YELLOW)
        emitted_label.next_to(radar_wave_out.get_center(), UP+RIGHT, buff=0.3)
        
        reflected_label = Text("Signal rétrodiffusé", font_size=20, color=RED)
        reflected_label.next_to(radar_wave_back.get_center(), UP+LEFT, buff=0.3)
        
        # Animation du schéma radar
        self.play(
            Create(radar),
            Create(radar_dish),
            Create(ground),
            run_time=1.5
        )
        
        # Visualiser l'émission de l'onde
        self.play(Create(radar_wave_out), run_time=1)
        self.play(Write(emitted_label), run_time=0.5)
        self.wait(0.5)
        
        # Visualiser la réflexion de l'onde
        self.play(Create(radar_wave_back), run_time=1)
        self.play(Write(reflected_label), run_time=0.5)
        self.wait(1)
        
        # Introduction au coefficient de rétrodiffusion
        backscatter_title = Text("Coefficient de rétrodiffusion (σ°)", font_size=28, color=GREEN)
        backscatter_title.to_edge(RIGHT).shift(UP * 1.5 + LEFT * 3)
        
        backscatter_def = BulletedList(
            "Mesure l'intensité du signal retourné vers le capteur",
            "Exprimé en décibels (dB)",
            "Dépend des propriétés de la surface",
            font_size=22
        )
        backscatter_def.next_to(backscatter_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Animation de la définition du coefficient de rétrodiffusion
        self.play(Write(backscatter_title), run_time=1)
        self.play(Write(backscatter_def), run_time=2)
        self.wait(1.5)
        
        # Formule du coefficient de rétrodiffusion (simplifiée)
        formula = MathTex(
            r"\sigma^{\circ} \propto", r" K_{s}", r" \cdot", r" \varepsilon_r",
            font_size=32
        )
        formula[1].set_color(YELLOW)  # Ks
        formula[3].set_color(BLUE)    # εr
        formula.next_to(backscatter_def, DOWN, buff=0.5)
        
        formula_explanation = VGroup(
            Text("Où:", font_size=22),
            MathTex(r"K_{s}", r"= \text{facteur de rugosité}", font_size=22),
            MathTex(r"\varepsilon_r", r"= \text{permittivité relative (liée à l'humidité)}", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT)
        formula_explanation[1][0].set_color(YELLOW)
        formula_explanation[2][0].set_color(BLUE)
        formula_explanation.next_to(formula, DOWN, buff=0.3)
        
        # Animation de la formule
        self.play(Write(formula), run_time=1.5)
        self.play(Write(formula_explanation), run_time=2)
        self.wait(2)
        
        # Transition vers la prochaine scène
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )


class SoilRoughnessEffect(Scene):
    """
    Cette classe illustre l'effet de la rugosité du sol sur le coefficient de rétrodiffusion
    """
    def construct(self):
        # Titre
        title = Text("1.1 Sensibilité du signal radar à la rugosité du sol", font_size=36)
        self.play(Write(title), run_time=1.5)
        self.play(title.animate.scale(0.8).to_edge(UP), run_time=1)
        
        # Définir les axes pour le graphique de rugosité vs coefficient de rétrodiffusion
        axes = Axes(
            x_range=[0, 1.5, 0.5],
            y_range=[-20, 0, 5],
            axis_config={"include_tip": True, "include_numbers": True},
            x_length=6,
            y_length=4
        )
        axes.to_edge(LEFT, buff=1)
        
        # Étiquettes des axes
        x_label = axes.get_x_axis_label(r"Rugosité ($K_s$)", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label(r"Coefficient de rétrodiffusion ($\sigma^{\circ}$) en dB", edge=LEFT, direction=LEFT)
        y_label.scale(0.8)
        
        # Fonction de coefficient de rétrodiffusion vs rugosité pour une humidité constante
        # Pour angle d'incidence 20°
        def backscatter_vs_roughness_20deg(x):
            # Simulation simplifiée basée sur les données fournies
            base = -15  # valeur de base en dB
            return base + 10 * np.log10(x * 2.5)
        
        # Pour angle d'incidence 40°
        def backscatter_vs_roughness_40deg(x):
            # Simulation simplifiée basée sur les données fournies
            base = -18  # valeur de base en dB
            return base + 10 * np.log10(x * 3.0)
        
        # Créer les courbes
        curve_20deg = axes.plot(backscatter_vs_roughness_20deg, color=RED, x_range=[0.1, 1.3])
        curve_40deg = axes.plot(backscatter_vs_roughness_40deg, color=BLUE, x_range=[0.1, 1.3])
        
        # Ajouter des étiquettes aux courbes
        curve_label_20deg = Text("Angle d'incidence 20°", font_size=20, color=RED)
        curve_label_20deg.next_to(curve_20deg.point_from_proportion(0.9), UP)
        
        curve_label_40deg = Text("Angle d'incidence 40°", font_size=20, color=BLUE)
        curve_label_40deg.next_to(curve_40deg.point_from_proportion(0.9), DOWN)
        
        # Animation des axes et courbes
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        
        self.play(
            Create(curve_20deg),
            Write(curve_label_20deg),
            run_time=1.5
        )
        
        self.play(
            Create(curve_40deg),
            Write(curve_label_40deg),
            run_time=1.5
        )
        
        # Marquer les points spécifiques mentionnés dans le texte
        # Point pour Ks = 0.4 (faible rugosité)
        low_roughness_20deg = axes.coords_to_point(LOW_ROUGHNESS_Ks, backscatter_vs_roughness_20deg(LOW_ROUGHNESS_Ks))
        low_roughness_dot_20deg = Dot(low_roughness_20deg, color=RED)
        
        low_roughness_40deg = axes.coords_to_point(LOW_ROUGHNESS_Ks, backscatter_vs_roughness_40deg(LOW_ROUGHNESS_Ks))
        low_roughness_dot_40deg = Dot(low_roughness_40deg, color=BLUE)
        
        low_roughness_label = MathTex(r"K_s = 0.4", font_size=24)
        low_roughness_label.next_to(low_roughness_dot_20deg, UP+LEFT)
        
        # Point pour Ks = 1.2 (forte rugosité)
        high_roughness_20deg = axes.coords_to_point(HIGH_ROUGHNESS_Ks, backscatter_vs_roughness_20deg(HIGH_ROUGHNESS_Ks))
        high_roughness_dot_20deg = Dot(high_roughness_20deg, color=RED)
        
        high_roughness_40deg = axes.coords_to_point(HIGH_ROUGHNESS_Ks, backscatter_vs_roughness_40deg(HIGH_ROUGHNESS_Ks))
        high_roughness_dot_40deg = Dot(high_roughness_40deg, color=BLUE)
        
        high_roughness_label = MathTex(r"K_s = 1.2", font_size=24)
        high_roughness_label.next_to(high_roughness_dot_20deg, UP+RIGHT)
        
        # Animation des points spécifiques
        self.play(
            Create(low_roughness_dot_20deg),
            Create(low_roughness_dot_40deg),
            Write(low_roughness_label),
            run_time=1
        )
        
        self.play(
            Create(high_roughness_dot_20deg),
            Create(high_roughness_dot_40deg),
            Write(high_roughness_label),
            run_time=1
        )
        
        # Illustration visuelle des surfaces de différentes rugosités
        # Surface peu rugueuse
        smooth_surface = FunctionGraph(
            lambda x: 0.05 * np.sin(10 * x),
            x_range=[-3, 3],
            color=BROWN
        )
        smooth_surface.scale(0.5).move_to(axes.coords_to_point(0.4, -26))
        
        smooth_label = Text("Surface faiblement rugueuse", font_size=20)
        smooth_label.next_to(smooth_surface, DOWN)
        
        # Surface très rugueuse
        rough_surface = FunctionGraph(
            lambda x: 0.2 * np.sin(10 * x) + 0.1 * np.sin(20 * x),
            x_range=[-3, 3],
            color=BROWN
        )
        rough_surface.scale(0.5).move_to(axes.coords_to_point(1.2, -26))
        
        rough_label = Text("Surface très rugueuse", font_size=20)
        rough_label.next_to(rough_surface, DOWN)
        
        # Animation des surfaces
        self.play(
            Create(smooth_surface),
            Write(smooth_label),
            run_time=1.5
        )
        
        self.play(
            Create(rough_surface),
            Write(rough_label),
            run_time=1.5
        )
        
        # Explication textuelle
        explanation = Text(
            "La rétrodiffusion radar augmente avec la rugosité de surface",
            font_size=24
        )
        explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(2)
        
        # Transition vers la prochaine scène
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )


class SoilMoistureEffect(Scene):
    """
    Cette classe illustre l'effet de l'humidité du sol sur le coefficient de rétrodiffusion
    """
    def construct(self):
        # Titre
        title = Text("1.2 Sensibilité du signal radar à l'humidité du sol", font_size=36)
        self.play(Write(title), run_time=1.5)
        self.play(title.animate.scale(0.8).to_edge(UP), run_time=1)
        
        # Définir les axes pour le graphique d'humidité vs coefficient de rétrodiffusion
        axes = Axes(
            x_range=[0, 40, 10],
            y_range=[-25, 0, 5],
            axis_config={"include_tip": True, "include_numbers": True},
            x_length=6,
            y_length=4
        )
        axes.to_edge(LEFT, buff=1)
        
        # Étiquettes des axes
        x_label = axes.get_x_axis_label(r"Humidité volumique du sol (%)", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label(r"Coefficient de rétrodiffusion ($\sigma^{\circ}$) en dB", edge=LEFT, direction=LEFT)
        y_label.scale(0.8)
        
        # Fonction de coefficient de rétrodiffusion vs humidité pour différentes rugosités
        # Pour faible rugosité (Ks = 0.4)
        def backscatter_vs_moisture_low_roughness(x):
            # Simulation simplifiée basée sur les données du document
            base = -22  # valeur de base en dB
            # Relation non linéaire avec saturation à des valeurs élevées d'humidité
            sensitivity = 0.8 - (x/100) * 0.6  # sensibilité diminue avec l'humidité
            return base + sensitivity * 15 * np.log10(1 + x/5)
        
        # Pour forte rugosité (Ks = 1.2)
        def backscatter_vs_moisture_high_roughness(x):
            # Simulation simplifiée basée sur les données du document
            base = -15  # valeur de base en dB
            # Relation non linéaire avec saturation à des valeurs élevées d'humidité
            sensitivity = 0.8 - (x/100) * 0.6  # sensibilité diminue avec l'humidité
            return base + sensitivity * 12 * np.log10(1 + x/5)
        
        # Créer les courbes
        curve_low_roughness = axes.plot(backscatter_vs_moisture_low_roughness, color=BLUE, x_range=[0.1, 40])
        curve_high_roughness = axes.plot(backscatter_vs_moisture_high_roughness, color=RED, x_range=[0.1, 40])
        
        # Ajouter des étiquettes aux courbes
        curve_label_low_roughness = Text("Faible rugosité (Ks = 0.4)", font_size=20, color=BLUE)
        curve_label_low_roughness.next_to(axes, RIGHT).shift(UP * 1)
        
        curve_label_high_roughness = Text("Forte rugosité (Ks = 1.2)", font_size=20, color=RED)
        curve_label_high_roughness.next_to(curve_label_low_roughness, DOWN, aligned_edge=LEFT)
        
        # Animation des axes et courbes
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        
        self.play(
            Create(curve_low_roughness),
            Write(curve_label_low_roughness),
            run_time=1.5
        )
        
        self.play(
            Create(curve_high_roughness),
            Write(curve_label_high_roughness),
            run_time=1.5
        )
        
        # Points et lignes de référence pour montrer la sensibilité
        # Pour la faible rugosité à humidité faible (5%)
        low_moisture_point_1 = axes.coords_to_point(5, backscatter_vs_moisture_low_roughness(5))
        dot_low_moisture_1 = Dot(low_moisture_point_1, color=BLUE)
        
        # Pour la faible rugosité à humidité moyenne (15%)
        mid_moisture_point_1 = axes.coords_to_point(15, backscatter_vs_moisture_low_roughness(15))
        dot_mid_moisture_1 = Dot(mid_moisture_point_1, color=BLUE)
        
        # Ligne de référence pour montrer l'augmentation
        line_reference_1 = Line(low_moisture_point_1, mid_moisture_point_1, color=YELLOW)
        
        # Valeur d'augmentation (en dB)
        increase_1 = backscatter_vs_moisture_low_roughness(15) - backscatter_vs_moisture_low_roughness(5)
        increase_label_1 = Text(f"Δσ° = {increase_1:.1f} dB", font_size=20, color=YELLOW)
        increase_label_1.next_to(line_reference_1.get_center(), UP)
        
        # Animation des points et lignes de référence
        self.play(
            Create(dot_low_moisture_1),
            Create(dot_mid_moisture_1),
            run_time=1
        )
        
        self.play(
            Create(line_reference_1),
            Write(increase_label_1),
            run_time=1.5
        )
        
        # Pour la faible rugosité à humidité élevée (30%)
        high_moisture_point_1 = axes.coords_to_point(30, backscatter_vs_moisture_low_roughness(30))
        dot_high_moisture_1 = Dot(high_moisture_point_1, color=BLUE)
        
        # Ligne de référence pour montrer l'augmentation
        line_reference_2 = Line(mid_moisture_point_1, high_moisture_point_1, color=GREEN)
        
        # Valeur d'augmentation (en dB)
        increase_2 = backscatter_vs_moisture_low_roughness(30) - backscatter_vs_moisture_low_roughness(15)
        increase_label_2 = Text(f"Δσ° = {increase_2:.1f} dB", font_size=20, color=GREEN)
        increase_label_2.next_to(line_reference_2.get_center(), UP)
        
        # Animation des points et lignes de référence
        self.play(
            Create(dot_high_moisture_1),
            run_time=1
        )
        
        self.play(
            Create(line_reference_2),
            Write(increase_label_2),
            run_time=1.5
        )
        
        # Explication de la relation non linéaire
        explanation = VGroup(
            Text("Relation non linéaire:", font_size=24, color=YELLOW),
            BulletedList(
                "Forte sensibilité à faible humidité",
                "Saturation à forte humidité",
                font_size=22
            )
        ).arrange(DOWN, aligned_edge=LEFT)
        explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=2)
        self.wait(2)
        
        # Permittivité diélectrique
        permittivity_title = Text("Permittivité diélectrique (εr)", font_size=28, color=BLUE)
        permittivity_title.to_edge(RIGHT).shift(LEFT * 3 + UP * 1)
        
        permittivity_equation = MathTex(r"\varepsilon_r \propto", r" \text{humidité du sol}", font_size=24)
        permittivity_equation.next_to(permittivity_title, DOWN)
        
        # Valeurs typiques
        permittivity_values = VGroup(
            Text("Sol sec: εr ≈ 3-8", font_size=22),
            Text("Sol saturé: εr ≈ 80", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT)
        permittivity_values.next_to(permittivity_equation, DOWN, buff=0.5)
        
        # Animation de la permittivité
        self.play(
            Write(permittivity_title),
            run_time=1
        )
        
        self.play(
            Write(permittivity_equation),
            run_time=1.5
        )
        
        self.play(
            Write(permittivity_values),
            run_time=1.5
        )
        
        self.wait(2)
        
        # Transition vers la prochaine scène
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )


class IncidenceAngleEffect(Scene):
    """
    Cette classe illustre les différences entre les angles d'incidence (20° et 40°)
    """
    def construct(self):
        # Titre
        title = Text("1.3 Différences entre les deux angles d'incidence", font_size=36)
        self.play(Write(title), run_time=1.5)
        self.play(title.animate.scale(0.8).to_edge(UP), run_time=1)
        
        # Représentation visuelle des angles d'incidence
        # Sol
        ground = Line(LEFT * 6, RIGHT * 6, color=BROWN_B)
        ground.move_to(DOWN * 2)
        
        # Point d'incidence
        incidence_point = ground.point_from_proportion(0.5)
        incidence_dot = Dot(incidence_point, color=WHITE)
        
        # Angles d'incidence
        # 20 degrés
        satellite_20deg = Dot(incidence_point + UP * 3 + RIGHT * 1.1, color=RED)
        ray_20deg = Line(satellite_20deg.get_center(), incidence_point, color=RED)
        
        angle_20deg_arc = Arc(
            radius=1,
            start_angle=-PI/2,
            angle=PI/9,  # 20 degrés en radians
            color=RED
        )
        angle_20deg_arc.move_to(incidence_point)
        
        angle_20deg_label = Text("20°", font_size=24, color=RED)
        angle_20deg_label.next_to(angle_20deg_arc, RIGHT)
        
        # 40 degrés
        satellite_40deg = Dot(incidence_point + UP * 2.3 + RIGHT * 1.9, color=BLUE)
        ray_40deg = Line(satellite_40deg.get_center(), incidence_point, color=BLUE)
        
        angle_40deg_arc = Arc(
            radius=0.7,
            start_angle=-PI/2,
            angle=PI/4.5,  # 40 degrés en radians
            color=BLUE
        )
        angle_40deg_arc.move_to(incidence_point)
        
        angle_40deg_label = Text("40°", font_size=24, color=BLUE)
        angle_40deg_label.next_to(angle_40deg_arc, RIGHT)
        
        # Animation de la représentation visuelle
        self.play(
            Create(ground),
            Create(incidence_dot),
            run_time=1
        )
        
        self.play(
            Create(ray_20deg),
            Create(satellite_20deg),
            Create(angle_20deg_arc),
            Write(angle_20deg_label),
            run_time=1.5
        )
        
        self.play(
            Create(ray_40deg),
            Create(satellite_40deg),
            Create(angle_40deg_arc),
            Write(angle_40deg_label),
            run_time=1.5
        )
        
        # Différences clés - Boîte d'explication
        explanation_box = Rectangle(width=6, height=3.5, color=YELLOW_B)
        explanation_box.set_fill(BLACK, opacity=0.7)
        explanation_box.to_edge(RIGHT, buff=0.5)
        
        explanation_title = Text("Différences clés:", font_size=28, color=YELLOW)
        explanation_title.next_to(explanation_box.get_top(), DOWN, buff=0.3)
        
        explanation_text = BulletedList(
            "Valeurs de σ° plus faibles à 40° qu'à 20°",
            "Meilleure discrimination des rugosités à 40°",
            "Sensibilité à l'humidité légèrement moindre à 40°",
            "Signal traverse plus de matière à 40°",
            font_size=20
        )
        explanation_text.next_to(explanation_title, DOWN, buff=0.3)
        
        # Animation de l'explication
        self.play(
            Create(explanation_box),
            Write(explanation_title),
            run_time=1
        )
        
        self.play(
            Write(explanation_text),
            run_time=2
        )
        
        # Illustration de la profondeur de pénétration
        # 20 degrés - pénétration moins profonde
        penetration_20deg = Line(incidence_point, incidence_point + DOWN * 0.7, color=RED, stroke_width=4)
        penetration_20deg_label = Text("Pénétration à 20°", font_size=20, color=RED)
        penetration_20deg_label.next_to(penetration_20deg, LEFT)
        
        # 40 degrés - pénétration plus profonde
        penetration_40deg = Line(incidence_point, incidence_point + DOWN * 0.4, color=BLUE, stroke_width=4)
        penetration_40deg_label = Text("Pénétration à 40°", font_size=20, color=BLUE)
        penetration_40deg_label.next_to(penetration_40deg, RIGHT)
        
        # Animation de la pénétration
        self.play(
            Create(penetration_20deg),
            Write(penetration_20deg_label),
            run_time=1.5
        )
        
        self.play(
            Create(penetration_40deg),
            Write(penetration_40deg_label),
            run_time=1.5
        )
        
        # Explication finale
        final_explanation = Text(
            "À 40°, le signal radar traverse davantage de matière avant d'atteindre le sol,\n"
            "réduisant sa sensibilité à l'humidité du sol, particulièrement sous la végétation.",
            font_size=24,
            t2c={"40°": BLUE, "sensibilité": YELLOW}
        )
        final_explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_explanation), run_time=2)
        self.wait(2)
        
        # Transition vers la prochaine scène
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )


class SoilMoistureRadarConclusion(Scene):
    """
    Cette classe présente la conclusion et les applications de la télédétection radar
    pour l'humidité du sol
    """
    def construct(self):
        # Titre
        title = Text("Applications de la télédétection de l'humidité du sol", font_size=42)
        self.play(Write(title), run_time=1.5)
        self.play(title.animate.scale(0.7).to_edge(UP), run_time=1)
        
        # Applications
        applications = VGroup(
            Text("Agriculture", font_size=32, color=GREEN),
            BulletedList(
                "Optimisation de l'irrigation",
                "Prévisions de rendement",
                "Détection précoce de stress hydrique",
                font_size=24
            ),
            
            Text("Gestion des ressources en eau", font_size=32, color=BLUE),
            BulletedList(
                "Prévision des inondations",
                "Gestion des bassins versants",
                "Suivi des sécheresses",
                font_size=24
            ),
            
            Text("Sciences climatiques", font_size=32, color=RED),
            BulletedList(
                "Modélisation du cycle de l'eau",
                "Études des changements climatiques",
                "Surveillance environnementale",
                font_size=24
            )
        )
        
        # Organiser les applications en colonnes
        applications[0].to_edge(LEFT, buff=1).shift(UP * 1.5)
        applications[1].next_to(applications[0], DOWN, buff=0.3)
        
        applications[2].to_corner(UP).shift(DOWN * 0.5)
        applications[3].next_to(applications[2], DOWN, buff=0.3)
        
        applications[4].to_edge(RIGHT, buff=1).shift(UP * 1.5)
        applications[5].next_to(applications[4], DOWN, buff=0.3)
        
        # Animation des applications
        self.play(
            Write(applications[0]),
            run_time=1
        )
        self.play(
            Write(applications[1]),
            run_time=1.5
        )
        
        self.play(
            Write(applications[2]),
            run_time=1
        )
        self.play(
            Write(applications[3]),
            run_time=1.5
        )
        
        self.play(
            Write(applications[4]),
            run_time=1
        )
        self.play(
            Write(applications[5]),
            run_time=1.5
        )
        
        # Satellites et capteurs radar utilisés
        satellites_title = Text("Satellites & capteurs radar", font_size=32, color=YELLOW)
        satellites_title.to_edge(DOWN, buff=2)
        
        satellites = VGroup(
            Text("Sentinel-1 (ESA)", font_size=24),
            Text("RADARSAT-2 (Canada)", font_size=24),
            Text("ALOS-2 PALSAR (Japon)", font_size=24),
            Text("TerraSAR-X (Allemagne)", font_size=24)
        ).arrange(RIGHT, buff=0.5)
        satellites.next_to(satellites_title, DOWN, buff=0.3)
        
        # Animation des satellites
        self.play(
            Write(satellites_title),
            run_time=1
        )
        self.play(
            Write(satellites),
            run_time=2
        )
        
        # Conclusion finale
        conclusion = Text(
            "La télédétection radar offre une solution efficace pour surveiller\n"
            "l'humidité du sol à grande échelle, de jour comme de nuit\n"
            "et dans la plupart des conditions météorologiques.",
            font_size=28,
            t2c={"télédétection radar": YELLOW, "grande échelle": GREEN}
        )
        conclusion.to_edge(DOWN, buff=0.5)
        
        self.play(
            Write(conclusion),
            run_time=2
        )
        self.wait(3)


class SoilMoistureWithRadar(Scene):
    """
    Scène principale qui enchaîne toutes les scènes précédentes
    """
    def construct(self):
        # Créer toutes les scènes
        scenes = [
            RadarBasics(),
            SoilRoughnessEffect(),
            SoilMoistureEffect(),
            IncidenceAngleEffect(),
            SoilMoistureRadarConclusion()
        ]
        
        # Jouer chaque scène
        for scene in scenes:
            for animation in scene.animations:
                self.play(animation)


# Si ce fichier est exécuté directement
if __name__ == "__main__":
    print("Ce fichier contient des animations sur l'humidité du sol avec radar.")
    print("Utilisez manim pour les exécuter, par exemple:")
    print("manim -pqh soil_moisture_radar.py RadarBasics")
    print("manim -pqh soil_moisture_radar.py SoilRoughnessEffect")
    print("manim -pqh soil_moisture_radar.py SoilMoistureEffect")
    print("manim -pqh soil_moisture_radar.py IncidenceAngleEffect")
    print("manim -pqh soil_moisture_radar.py SoilMoistureRadarConclusion")
