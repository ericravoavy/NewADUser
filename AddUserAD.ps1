#Creating PSobject model with information properties of a new employee.
#These informations should be provided by HR departement

param(
    $csvpath
)

# affecter les valeurs des attributs du fichier csv dans la variable users
$users = Import-Csv -Delimiter ";" -Path $csvpath

# Description de la class user
$Userclass = New-Object psobject -Property @{
    name = $null
    first_name = $null
    last_name = $null
    samaccountname = $null
    login = $null
    Tel_number = $null
    mail_address = $null
    departement = $null
    job_title = $null
    OUPath = $null
    Enable = $null
}

# Contructor of userclass class
# define the mandatory information parameters of the object
function Userclass {
    param(
        [Parameter(Mandatory=$true)]
        [String]$name,
        [Parameter(Mandatory=$true)]
        [String]$first_name,
        [Parameter(Mandatory=$true)]
        [string]$last_name,
        [parameter(Mandatory=$true)]
        [string]$samaccountname,
        [parameter(Mandatory=$true)]
        [string]$login,
        [Parameter(Mandatory=$false)]
        [long]$Tel_number,
        [Parameter(Mandatory=$false)]
        [string]$mail_address,
        [Parameter(Mandatory=$false)]
        #[ValidateSet('CA','Treasury','IT','Finance')]
        [String]$departement,
        [Parameter(Mandatory=$false)]
        #[ValidateSet('IT','Accountant','VP','AVP')]
        [string]$job_title,
        [Parameter(Mandatory=$false)]
        [string]$OUPath,
        [Parameter(Mandatory=$false)]
        [string]$Enable
    )
    $Userclass = $Userclass.psobject.copy()
    $Userclass.name = $first_name+ " " + $name
    $Userclass.first_name = $first_name
    $Userclass.last_name = $last_name
    $Userclass.samaccountname = $samaccountname
    $Userclass.login = $login
    $Userclass.Tel_number = $Tel_number
    $Userclass.mail_address = $mail_address
    $Userclass.departement = $departement
    $Userclass.job_title = $job_title
    $userclass.OUPath = $OUPath
    $userclass.Enable = $Enable
    $Userclass
}

# affectation de chaque attribut de chaques ligne du csv dans le variable user
foreach($user in $users)
{
    $name = $user.firstname + " " + $user.lastname
    $fname = $user.firstname
    $lname = $user.lastname
    $login = $user.firstname + "." + $user.lastname
    $officephone = $user.tel_number
    $mobilephone = $user.mobile_number
    $job_title = $user.job_title
    $dept = $user.departement
    $email = $email
    $Upassword = "Welcome.2020"
    $OUPath = "OU=Laptop Users,OU=Users,OU=SH,DC=silver-holdings,DC=lan"

    # Fonction de creation de compte dans l'Active Directory avec une condition de réussite ou echec
    try {
            New-ADUser -Name $name -Surname $lname -GivenName $fname -Path $OUPath -SamAccountName $login `
            -UserPrincipalName $login -DisplayName $name -OfficePhone $officephone `
            -MobilePhone $mobilephone -Title $job_title `
            -AccountPassword (ConvertTo-SecureString $Upassword -AsPlainText -Force) `
            -Department $dept -Enable $true `
            -ChangePasswordAtLogon $true
            Write-Output "Users below has been added in AD :"
            Write-Output "User Added : $name login : $login Phone number : $officephone email = $email "
    }catch{
        Write-Output "Error : User $name has not been added"
        }
}