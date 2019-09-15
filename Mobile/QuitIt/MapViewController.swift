
import UIKit
import MapKit
import CoreLocation


class MapViewController: UIViewController, CLLocationManagerDelegate {
    
    var locationManager = CLLocationManager()
    
    @IBOutlet weak var mapView: MKMapView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        mapView.register(MKMarkerAnnotationView.self, forAnnotationViewWithReuseIdentifier: MKMapViewDefaultAnnotationViewReuseIdentifier)
        
        self.locationManager.requestWhenInUseAuthorization()
        
        if CLLocationManager.locationServicesEnabled(){
            locationManager.delegate = self
            locationManager.desiredAccuracy = kCLLocationAccuracyNearestTenMeters
            locationManager.startUpdatingLocation()
        }
        
        createAnnotations(locations: annotationLocations)
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let locValue: CLLocationCoordinate2D = manager.location!.coordinate
        //locValue.latitude locValue.longitude
//        let userLocation = locations.last
//        let viewRegion = MKCoordinateRegion(center: (userLocation?.coordinate)!, latitudinalMeters: 600,longitudinalMeters: 600)
//        self.mapView.setRegion(viewRegion, animated: true)
    }
    
    
    let annotationLocations = [
        ["title": "Student Center", "latitude": 42.359050, "longitude": -71.094760],

    ]
    func createAnnotations(locations: [[String: Any]]) {
                for location in locations{
                    let annotations = MKPointAnnotation()
                    annotations.title = location["title"] as? String
                    annotations.coordinate = CLLocationCoordinate2D(latitude: location["latitude"] as! CLLocationDegrees, longitude: location["longitude"] as! CLLocationDegrees)
                    mapView.addAnnotation(annotations)
        }
        
        var region: MKCoordinateRegion{
            let span = MKCoordinateSpan(latitudeDelta: 0.005, longitudeDelta: 0.005)
            let chapelCoordinate = CLLocationCoordinate2D(latitude: 42.359050, longitude: -71.094760)
            return MKCoordinateRegion(center: chapelCoordinate, span: span)
        }
        mapView.setRegion(region, animated: true)
        
    }
}
