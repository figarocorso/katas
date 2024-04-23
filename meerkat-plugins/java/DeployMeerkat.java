public class DeployMeerkat {
    public static void deployCloudInfra() {
        System.out.println("Cloud infra deployed");
    }

    public static void deployMeerkat() {
        System.out.println("Application deployed");
    }

    public static void main(String[] args) {
        deployCloudInfra();
        deployMeerkat();
    }
}
