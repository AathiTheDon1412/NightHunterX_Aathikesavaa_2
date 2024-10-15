const generateButton = document.getElementById("generate-btn");
const resultContainer = document.getElementById("result-container");

generateButton.addEventListener("click", async () => {
    const description = document.getElementById("description").value.trim();

    if (description) {
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: description })
            });

            const data = await response.json();
            if (data.model_path) {
                loadModel(data.model_path);
            } else {
                resultContainer.innerHTML = '<p>Error generating model.</p>';
            }
        } catch (error) {
            console.error(error);
            resultContainer.innerHTML = '<p>Error generating 3D model.</p>';
        }
    } else {
        resultContainer.innerHTML = '<p>Please enter a text description.</p>';
    }
});

function loadModel(modelPath) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('3d-container').innerHTML = ''; // Clear previous model
    document.getElementById('3d-container').appendChild(renderer.domElement);

    const loader = new THREE.OBJLoader();
    loader.load(modelPath, function (object) {
        scene.add(object);
        animate();
    });

    camera.position.z = 5;

    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
}